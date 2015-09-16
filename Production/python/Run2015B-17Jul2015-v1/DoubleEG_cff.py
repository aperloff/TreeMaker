import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/02FC1E69-AF2E-E511-ABA6-0025905B858E.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/0647ED4F-AB2E-E511-AB06-002618943885.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/0AC1734F-AC2E-E511-A5E0-0025905964BE.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/0EF0278F-AD2E-E511-87A5-002354EF3BD2.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/129C3701-AE2E-E511-8CA0-0025905B858C.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/140EDB4E-AD2E-E511-A7BD-0025905B8596.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/140F3DCE-AC2E-E511-B99F-0025905A60E4.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/14A76A49-AD2E-E511-AC70-003048FFD728.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/1615789D-AE2E-E511-A7F1-002618FDA28E.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/18AD5790-AB2E-E511-95CA-002618943960.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/1AD60D9C-AF2E-E511-AC41-00261894386C.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/1AF5F547-AC2E-E511-B0FC-00248C55CC9D.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/1C464774-AE2E-E511-B86B-0025905A497A.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/1CCCBC7B-AB2E-E511-822B-002618943902.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/26EA206B-AD2E-E511-A542-0025905A48BB.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/286AA0D1-AE2E-E511-AA8F-002618943896.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/2A4257B0-AD2E-E511-A487-0025905A48B2.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/302BF9E9-AB2E-E511-BE9C-0025905A60B2.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/30AED9C6-AC2E-E511-94A2-00261894386F.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/30D27BCE-AC2E-E511-8AF6-002590596486.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/366BEA48-AC2E-E511-86A7-0025905B8576.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/36F9BDC7-AD2E-E511-A3FE-002618943960.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/3C853FCC-AE2E-E511-AEE2-0025905B85AA.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/403E9533-AD2E-E511-BD69-0025905B85EE.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/46805591-AB2E-E511-8B4D-002618943902.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/482D229F-AE2E-E511-B28F-00261894386E.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/4858D65E-AB2E-E511-9A3B-0025905A610A.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/4A415E09-AC2E-E511-B46B-003048FFD760.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/54932169-AF2E-E511-9D7A-0025905A6132.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/561B8650-AC2E-E511-851C-0025905B8610.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/58B7075C-AE2E-E511-B33A-003048FFCC18.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/5C823533-AD2E-E511-B76C-0025905A60B2.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/5E0C02A3-AD2E-E511-8C3F-003048FFD752.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/5E60461E-AE2E-E511-AADB-0025905A497A.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/6A709486-AE2E-E511-8010-0025905B85EE.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/6AD019D8-AE2E-E511-80C3-003048FFD728.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/6CC229B7-AD2E-E511-A78A-00259059642A.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/7299218C-AE2E-E511-AC38-0025905B8596.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/72D6DC4F-AC2E-E511-BE36-0025905B85AA.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/747ECE65-AF2E-E511-BC7B-0025905A612C.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/74E750A4-AD2E-E511-88C8-0025905964BE.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/78207886-AD2E-E511-BBBC-00261894386E.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/7AEAFDE8-AD2E-E511-967B-0026189438F2.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/7C94BF6A-AF2E-E511-9EFC-0025905A612A.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/80621463-AE2E-E511-9E4A-0025905A60F2.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/80625EA5-AE2E-E511-B424-0025905A60B2.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/8272C14F-AD2E-E511-A4C6-00261894386C.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/829A4CA8-AB2E-E511-B91F-0025905A60F8.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/82E3FD68-AF2E-E511-BC91-0025905B858E.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/869C6150-AC2E-E511-9481-0025905A60BC.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/8A0BC760-AF2E-E511-8816-002618943864.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/986A284A-AC2E-E511-8601-00261894386C.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/9895E187-AD2E-E511-B434-0025905A60BC.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/9EF005FD-AD2E-E511-B9D9-00261894386F.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/A0F86ECB-AD2E-E511-B2C6-0026189437EC.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/A262C24E-AC2E-E511-9ADA-0025905A48B2.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/A445B223-AD2E-E511-AE73-003048FFD796.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/A4B2EE07-AC2E-E511-AFD7-0025905B8576.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/A6DD13C8-AD2E-E511-82AF-002618B27F8A.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/A85D6A71-AE2E-E511-85E8-0025905A6110.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/A8DC1556-AE2E-E511-B1C0-0025905B85AA.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/AC5CD050-AC2E-E511-AFC8-003048FFD752.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/AE2AA44D-AC2E-E511-B26A-0025905B858C.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/B0A2EDCD-AE2E-E511-98F2-0025905B85AA.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/B23A27A1-AD2E-E511-80B9-0025905B8576.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/B41A5864-AF2E-E511-AD16-003048FFCBA4.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/B4A0089E-AD2E-E511-AB34-002618943960.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/B4E0E1B0-AE2E-E511-93F3-002354EF3BD2.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/B6C02AD1-AE2E-E511-B2D3-002618943957.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/BE77298D-AD2E-E511-9982-0025905B85AA.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/BEF268D2-AD2E-E511-99D2-0025905A48D6.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/C246678B-AD2E-E511-82E5-0025905B85EE.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/C275DC5D-AF2E-E511-A889-0026189438B4.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/C4AF5864-AF2E-E511-A7A5-003048FFD7BE.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/C4DCC950-AC2E-E511-BB49-00259059642A.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/C63EA7D0-AE2E-E511-A102-003048FFD730.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/C6DA5EA5-AE2E-E511-8609-0025905A48BB.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/C884C14D-AC2E-E511-97E0-0025905B8596.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/CC896BA3-AD2E-E511-945E-002618943902.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/CE87CC6D-AF2E-E511-B4D8-0025905A608C.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/CED51ECB-AC2E-E511-A62B-0025905A497A.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/D284E690-AD2E-E511-9A05-003048FFD760.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/D49C4863-AF2E-E511-8CA2-0025905A60A8.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/D4D1CABB-AE2E-E511-A8D8-002618943960.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/D4E4EC62-AF2E-E511-B74D-0025905A6104.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/D801DF29-AD2E-E511-B319-00248C55CC9D.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/D83F46D0-AC2E-E511-982D-0025905A6094.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/D8926FCC-AC2E-E511-A6CE-0025905A6110.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/DC806E52-AE2E-E511-83A5-00261894386C.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/E051AF76-AB2E-E511-B3C2-002618943960.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/E2F86908-AC2E-E511-800B-003048FFCC18.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/E601AA5E-AE2E-E511-BD67-0025905A60E4.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/E616E16D-AD2E-E511-BB52-0025905B85AA.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/E8A8CAC8-AC2E-E511-BF57-0026189438F2.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/EA7C49C7-AE2E-E511-BC17-002618943902.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/F02BAC22-AF2E-E511-9330-002618943960.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/F07ED3D5-AE2E-E511-96B6-0026189437EC.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/F0A4F55E-AB2E-E511-9A60-0025905A610A.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/F2409353-AD2E-E511-8E40-003048FFD730.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/F4F09D6D-AE2E-E511-B935-002590596486.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/FA378ACC-AC2E-E511-A84C-0025905A48F2.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/FA64B032-AD2E-E511-850E-0025905B8576.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/FABC822E-AF2E-E511-8F9B-003048FFD752.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/FC7A52A4-AE2E-E511-A499-003048FFD796.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/FCE99093-AD2E-E511-8BFD-002618943896.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/17Jul2015-v1/40000/FECFCF4F-AC2E-E511-8701-0025905822B6.root' ] );


secFiles.extend( [
               ] )
