class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s: return self._mask_email(s)
        else: return self._mask_phone(s)

    def _mask_email(self, s: str) -> str:
        name, domain = s.split("@", 1)
        name, domain = name.lower(), domain.lower()
        masked_name = f"{name[0]}*****{name[-1]}"
        return f"{masked_name}@{domain}"

    def _mask_phone(self, s: str) -> str:
        digits = [char for char in s if char.isdigit()]
        local_last4, country_prefix = "".join(digits[-4:]), ""
        country_len = len(digits) - 10
        if country_len < 0 or country_len > 3:
            raise ValueError("Invalid phone number length")

        country_prefix = ""
        if country_len > 0:
            country_prefix = "+" + ("*" * country_len) + "-"
        
        local_mask = f"***-***-{local_last4}"
        return f"{country_prefix}{local_mask}"
