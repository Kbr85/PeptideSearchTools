# -*- mode: python -*-

block_cipher = None


a = Analysis(['PeptideSearchTools.py'],
             pathex=['/Users/kenny/TEMP-GUI/BORRAR-PeptideSearchTools'],
             binaries=[],
             datas=[('RESOURCES', '.')],
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
          console=False,
		  icon='ndowed')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='PeptideSearchTools')
app = BUNDLE(coll,
             name='PeptideSearchTools.app',
             icon='',
             bundle_identifier=None,
             info_plist={
               'NSHighResolutionCapable': 'True',
               'NSPrincipleClass': 'NSApplication',
               'NSAppleScriptEnabled': False,
               'CFBundleShortVersionString': '1.1.0',
               'CFBundleDocumentTypes': [
                  {
                    'CFBundleTypeName': 'My File Format',
                    'CFBundleTypeIconFile': 'MyFileIcon.icns',
                    'LSItemContentTypes': ['com.example.myformat'],
                    'LSHandlerRank': 'Owner'
                    }
                ]
            },
            )