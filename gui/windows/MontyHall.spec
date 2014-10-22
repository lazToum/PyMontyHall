# -*- mode: python -*-
a = Analysis(['MontyHall.py'],
             pathex=['C:\\Users\\Lazaros\\Desktop'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='MontyHall.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False )
