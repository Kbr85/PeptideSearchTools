# -*- mode: python -*-

block_cipher = None


a = Analysis(['PeptideSearchTools.py'],
             pathex=['C:\\Users\\bravo\\Desktop\\SharedFolders\\BORRAR-PEPTIDESEARCHTOOLS'],
             binaries=[],
             datas=[('RESOURCES', 'RESOURCES/.')],
             hiddenimports=[],
             hookspath=[],
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
          [],
          exclude_binaries=True,
          name='PeptideSearchTools',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          icon='',
          console=False,
          version='version.txt')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='PeptideSearchTools')
