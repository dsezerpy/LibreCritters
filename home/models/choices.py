# Predefined platform options
SOCIAL_PLATFORM_CHOICES = [
    ('linktree', 'Linktree'),
    ('instagram', 'Instagram'),
    ('bluesky', 'Bluesky'),
    ('twitter', 'Twitter / X'),
    ('furaffinity', 'FurAffinity'),
    ('toyhouse', 'Toyhouse'),
    ('deviantart', 'DeviantArt'),
    ('artstation', 'ArtStation'),
    ('kofi', 'Ko-fi'),
    ('patreon', 'Patreon'),
    ('website', 'Personal Website'),
    ('other', 'Other'),
]

LICENSE_CHOICES = [
    ('CC0', 'CC0 1.0 Universal (Public Domain)'),
    ('CC_BY', 'CC BY 4.0 (Attribution)'),
    ('CC_BY_SA', 'CC BY-SA 4.0 (Attribution-ShareAlike)'),
    ('CC_BY_NC', 'CC BY-NC 4.0 (Attribution-NonCommercial)'),
    ('CC_BY_NC_SA', 'CC BY-NC-SA 4.0 (Attribution-NonCommercial-ShareAlike)'),
    ('CC_BY_ND', 'CC BY-ND 4.0 (Attribution-NoDerivatives)'),
    ('CC_BY_NC_ND', 'CC BY-NC-ND 4.0 (Attribution-NonCommercial-NoDerivatives)'),
    ('OPEN', 'Open Species'),
    ('CLOSED', 'Closed Species'),
]

TRAIT_TYPE_CHOICES = [
    ('core', 'Core Spec (Mandatory)'),
    ('modular', 'Modular / Optional Add-on'),
    ('variant', 'Anatomical Variant'),
]

FILE_TYPE_CHOICES = [
    ('psd', 'PSD / Clip Studio (Layered Art)'),
    ('blend', '3D Mesh (.blend / .glb)'),
    ('vector', 'Vector (.svg / .pdf)'),
    ('lineart', 'PNG Lineart / Base'),
    ('other', 'Other Source File'),
]