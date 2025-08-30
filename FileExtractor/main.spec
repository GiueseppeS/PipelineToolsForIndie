# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['main.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        ('copyapp.kv', '.'),                      # Main kv file
        ('modules/inputfield.kv', 'modules'),     # InputField kv file
        ('Core/core_logic.py', 'Core'),           # Core logic module
    ],
    hiddenimports=[
        'modules.inputfield',     # Add any other hidden imports here
        'Core.core_logic',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,           # <-- Disable console
    windowed=True,           # <-- Enable windowed mode
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)