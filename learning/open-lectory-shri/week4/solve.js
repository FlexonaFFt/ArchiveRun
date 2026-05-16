const yargs = require('yargs');
const fs = require('fs').promises;
const path = require('path');

// Вспомогательные функции
async function ensureDir(dirPath) {
    try {
        await fs.mkdir(dirPath, { recursive: true });
    } catch (err) {
        throw new Error(`Failed to create directory: ${err.message}`);
    }
}

async function fileExists(filePath) {
    try {
        await fs.access(filePath);
        return true;
    } catch {
        return false;
    }
}

async function readJson(filePath) {
    try {
        if (!await fileExists(filePath)) {
            throw new Error(`Configuration file not found: ${filePath}`);
        }
        const content = await fs.readFile(filePath, 'utf8');
        return JSON.parse(content);
    } catch (err) {
        throw new Error(`Failed to read JSON file: ${err.message}`);
    }
}

async function writeJson(filePath, data) {
    try {
        await fs.writeFile(filePath, JSON.stringify(data, null, 2));
    } catch (err) {
        throw new Error(`Failed to write JSON file: ${err.message}`);
    }
}

async function getProjectInfo(projectPath) {
    try {
        const pkgPath = path.join(projectPath, 'package.json');
        if (await fileExists(pkgPath)) {
            const pkg = await readJson(pkgPath);
            return {
                title: pkg.name || 'Project',
                description: pkg.description || 'Project description'
            };
        }
        return {
            title: 'Project',
            description: 'Project description'
        };
    } catch (err) {
        throw new Error(`Failed to get project info: ${err.message}`);
    }
}

function applyTemplate(template, data) {
    try {
        let result = template;
        for (const [key, value] of Object.entries(data)) {
            if (!key || !value) {
                throw new Error(`Invalid key-value pair in template data`);
            }
            result = result.replace(new RegExp(`{${key}}`, 'g'), value);
        }
        return result;
    } catch (err) {
        throw new Error(`Failed to apply template: ${err.message}`);
    }
}

async function getSubdirectories(dir) {
    try {
        const entries = await fs.readdir(dir, { withFileTypes: true });
        return entries
            .filter(entry => entry.isDirectory())
            .map(entry => path.join(dir, entry.name));
    } catch (err) {
        throw new Error(`Failed to read directory: ${err.message}`);
    }
}

async function validatePath(dirPath) {
    try {
        const absolutePath = path.resolve(dirPath);
        const stats = await fs.stat(absolutePath);
        if (!stats.isDirectory()) {
            throw new Error(`Path is not a directory: ${absolutePath}`);
        }
        return absolutePath;
    } catch (err) {
        throw new Error(`Invalid path: ${err.message}`);
    }
}

// Обработчик команды init
async function initCommand(argv) {
    try {
        const projectPath = await validatePath(argv.path || process.cwd());
        const docsDir = argv['docs-dir'] || 'docs';
        const configPath = path.join(projectPath, '.doc-tool.json');
        const docsPath = path.join(projectPath, docsDir);
        const readmePath = path.join(docsPath, 'README.md');

        // Создаем папку docs
        await ensureDir(docsPath);

        // Создаем README.md, если не существует или указан --force
        if (!await fileExists(readmePath) || argv.force) {
            const { title, description } = await getProjectInfo(projectPath);
            const readmeContent = `## ${title}\n### Описание\n${description}\n### Общие соглашения\n#### Coding standards\nFollow project coding standards`;
            await fs.writeFile(readmePath, readmeContent);
        }

        // Создаем конфиг, если не существует или указан --force
        if (!await fileExists(configPath) || argv.force) {
            const config = {
                docsDir,
                ignoreCoverage: ['node_modules', 'dist', 'build']
            };
            await writeJson(configPath, config);
        }
    } catch (err) {
        console.error(`Error: ${err.message}`);
    }
}

// Обработчик команды generate
async function generateCommand(argv) {
    try {
        const dirPath = await validatePath(argv.path || process.cwd());
        const projectPath = await validatePath(argv['project-path'] || process.cwd());
        const readmePath = path.join(dirPath, 'README.md');

        // Проверяем существование файла
        if (await fileExists(readmePath) && !argv.force) {
            throw new Error('README.md already exists');
        }

        // Определяем путь к шаблону
        let template = '## {title}\n## Описание\n{description}';
        if (argv['template-path']) {
            if (!await fileExists(argv['template-path'])) {
                throw new Error(`Template file not found: ${argv['template-path']}`);
            }
            template = await fs.readFile(argv['template-path'], 'utf8');
        } else {
            const configPath = path.join(projectPath, '.doc-tool.json');
            if (await fileExists(configPath)) {
                const config = await readJson(configPath);
                if (config.templatePath) {
                    if (!await fileExists(config.templatePath)) {
                        throw new Error(`Template file not found: ${config.templatePath}`);
                    }
                    template = await fs.readFile(config.templatePath, 'utf8');
                }
            }
        }

        // Формируем данные для шаблона
        let templateData = await getProjectInfo(projectPath);
        if (argv.set) {
            const sets = Array.isArray(argv.set) ? argv.set : [argv.set];
            for (const set of sets) {
                if (!set.includes('=')) {
                    throw new Error(`Invalid set format: ${set}. Expected key=value`);
                }
                const [key, value] = set.split('=');
                if (!key || !value) {
                    throw new Error(`Invalid key-value pair: ${set}`);
                }
                templateData[key] = value;
            }
        }

        // Применяем шаблон и записываем файл
        const content = applyTemplate(template, templateData);
        await fs.writeFile(readmePath, content);
    } catch (err) {
        console.error(`Error: ${err.message}`);
    }
}

// Обработчик команды coverage
async function coverageCommand(argv) {
    try {
        const projectPath = await validatePath(argv.path || process.cwd());
        const configPath = path.join(projectPath, '.doc-tool.json');
        let ignorePatterns = ['node_modules', 'dist', 'build'];

        // Читаем конфиг, если существует
        if (await fileExists(configPath)) {
            const config = await readJson(configPath);
            ignorePatterns = config.ignoreCoverage || ignorePatterns;
        }

        // Собираем все директории рекурсивно
        async function collectDirs(dir, allDirs = new Set()) {
            allDirs.add(dir);
            const subdirs = await getSubdirectories(dir);
            for (const subdir of subdirs) {
                await collectDirs(subdir, allDirs);
            }
            return allDirs;
        }

        const allDirs = await collectDirs(projectPath);
        const filteredDirs = [...allDirs].filter(dir => 
            !ignorePatterns.some(pattern => {
                const relativePath = path.relative(projectPath, dir);
                return relativePath === pattern || relativePath.startsWith(pattern + path.sep);
            })
        );

        // Проверяем наличие README.md
        const documented = [];
        const undocumented = [];
        for (const dir of filteredDirs) {
            const readmePath = path.join(dir, 'README.md');
            if (await fileExists(readmePath)) {
                documented.push(dir);
            } else {
                undocumented.push(path.relative(projectPath, dir) || '.');
            }
        }

        // Вычисляем процент покрытия
        const total = filteredDirs.length;
        const covered = documented.length;
        const percentage = total > 0 ? Math.round((covered / total) * 100) : 0;

        // Формируем отчет
        console.log(`Documentation coverage: ${percentage}% (${covered}/${total} directories)`);
        if (undocumented.length > 0) {
            console.log('\nUndocumented directories:');
            undocumented.forEach(dir => console.log(`- ${dir}`));
        }
    } catch (err) {
        console.error(`Error: ${err.message}`);
    }
}

// Настройка yargs
yargs
    .command('init [path]', 'Initialize documentation', yargs => {
        yargs
            .option('force', { alias: 'f', type: 'boolean', description: 'Overwrite existing files' })
            .option('docs-dir', { type: 'string', description: 'Documentation directory name' });
    }, initCommand)
    .command('generate [path]', 'Generate documentation', yargs => {
        yargs
            .option('project-path', { type: 'string', description: 'Project directory path' })
            .option('force', { alias: 'f', type: 'boolean', description: 'Overwrite existing README.md' })
            .option('template-path', { type: 'string', description: 'Template file path' })
            .option('set', { type: 'string', array: true, description: 'Key-value pairs for template' });
    }, generateCommand)
    .command('coverage [path]', 'Check documentation coverage', yargs => {}, coverageCommand)
    .strict()
    .help()
    .argv;
