# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['app.py'],
    pathex=['/Users/craig.bennett/.local/share/virtualenvs/kounter-mjjZWhnz/lib/python3.9/site-packages'],
    binaries=[],
    datas=[('/usr/local/lib/python3.9/site-packages','customtkinter'),
    ('/usr/local/lib/python3.9/site-packages/tkinterDnD','tkinterDnD'),
    ('/usr/local/lib/python3.9/site-packages/tkdnd','tkdnd'),
    ('/usr/local/lib/python3.9/site-packages/tk','tk')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='app',
)
