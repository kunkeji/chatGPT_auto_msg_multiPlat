# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['G:\\wwwroot\\aimsg2.1\\app.py'],
    pathex=[],
    binaries=[],
    datas=[('G:\\wwwroot\\aimsg2.1\\src\\ChatPage.py', '.'), ('G:\\wwwroot\\aimsg2.1\\src\\HomePage.py', '.'), ('G:\\wwwroot\\aimsg2.1\\src\\LogPage.py', '.'), ('G:\\wwwroot\\aimsg2.1\\src\\MainWindow.py', '.'), ('G:\\wwwroot\\aimsg2.1\\src\\MessageProcessor.py', '.'), ('G:\\wwwroot\\aimsg2.1\\src\\SettingsPage.py', '.'), ('G:\\wwwroot\\aimsg2.1\\utils\\utils.py', '.'), ('G:\\wwwroot\\aimsg2.1\\utils', 'utils/'), ('G:\\wwwroot\\aimsg2.1\\src', 'src/'), ('G:\\wwwroot\\aimsg2.1\\static', 'static/')],
    hiddenimports=[],
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
    name='壳林智能客服助手',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['G:\\wwwroot\\aimsg2.1\\logo.ico'],
)
