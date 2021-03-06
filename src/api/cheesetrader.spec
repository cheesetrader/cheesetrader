# -*- mode: python ; coding: utf-8 -*-

specpath = os.path.dirname(os.path.abspath(SPEC))
block_cipher = None

a = Analysis(['cheesetrader.py'],
             pathex=['C:\\projects\\sandbox\\test'],
             binaries=[],
             datas=[],
             hiddenimports=['numpy.core.multiarray',
             'uvicorn.logging',
             'uvicorn.loops',
             'uvicorn.loops.auto',
             'uvicorn.protocols',
             'uvicorn.protocols.http',
             'uvicorn.protocols.http.auto',
             'websockets.legacy',
             'websockets.legacy.server',
             'uvicorn.lifespan',
             'uvicorn.lifespan.on',
             'MetaTrader5',
             'cheesetrader'],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='cheesetrader',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          icon=os.path.join(specpath, 'cheese.ico'),
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
