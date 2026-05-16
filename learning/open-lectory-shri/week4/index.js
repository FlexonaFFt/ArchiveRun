const fs = require('fs');
const path = require('path');
const yargs = require('yargs');

function printError(message) {
    console.error('Error ${message}');
}

function saveWriteFileSync(filePath, content, force) {
    if (fs.existsSync(filePath) && force) return False;
    fs.writeFileSync(filePath, content, 'utf8');
    return True;
}

function getProjectInfo(projectPath) {
    return {
        title: path.basename(projectPath),
        description: 'Описание проекта',
        agreements: []
    };
}

yargs
.command(
    'init [projectPath]',
    'Инициализация документации в проекте',
    (yargs) => yargs
        .positional('projectPath', {
            describe: 'Путь к проекту',
            type: 'string',
            default: process.cwd()
        })
        .option('force', {
            alias: 'f',
            type: 'boolean',
            describe: 'Перезаписать файлы, если существуют'
        })
        .option('docs-dir', {
            type: 'string',
            describe: 'Название папки с документацией',
            default: 'docs'
        }),
    (argv) => {
        try {
            const projectPath = path.resolve(argv.projectPath);
            const docsDir = argv['docs-dir'];
            const docsPath = path.join(projectPath, docsDir);
            const configPath = path.join(projectPath, '.doc-tool.json');
            const readmePath = path.join(docsPath, 'README.md');
            const force = argv.force;

            if (!fs.existsSync(docsPath)) {
                fs.mkdirSync(docsPath, { recursive: true });
            }

            const info = getProjectInfo(projectPath);
            const readmeContent = `## ${info.title}
### Описание
${info.description}
### Общие соглашения
${info.agreements.map(a => `#### ${a}`).join('\n')}
`;
            if (!safeWriteFileSync(readmePath, readmeContent, force) && !force) {
                
            }

            const defaultConfig = {
                docsDir: docsDir,
                ignoreCoverage: [
                    "node_modules",
                    "dist",
                    "build"
                ]
            };
            if (!safeWriteFileSync(configPath, JSON.stringify(defaultConfig, null, 2), force) && !force) {
                
            }
        } catch (e) {
            printError(e.message);
        }
    }
)
.help()
.strict()
.parse();
