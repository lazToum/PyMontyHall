# -*- mode: python -*-
a = Analysis(['MontyHall.py'],
             pathex=['/media/lary/7606DE0606DDC6F1/Users/Lary/Desktop/Mega/monty'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='MontyHall',
          debug=False,
          strip=None,
          upx=True,
          console=True )
