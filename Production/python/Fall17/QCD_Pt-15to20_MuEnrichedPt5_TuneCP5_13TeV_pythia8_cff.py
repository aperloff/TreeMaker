import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/007C7261-3342-E811-9371-008CFAE45118.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/1AFA1DFE-2A42-E811-9580-008CFAC93C48.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/2095CB55-2542-E811-9D58-008CFAC9170C.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/22343F90-3A42-E811-8695-008CFAC91A4C.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/30002E47-2442-E811-9049-008CFA197D3C.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/3CF29913-2A42-E811-8DBF-008CFAC93B28.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/46254C4A-3142-E811-8A4D-008CFAE45438.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/4814A204-3042-E811-8ACD-008CFAC91A00.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/4C172BBE-2742-E811-BE20-008CFA1974B4.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/52831373-2C42-E811-A443-008CFAC93B2C.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/5E6C9717-2842-E811-BCCF-008CFAC93DC4.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/60A34213-2A42-E811-BFB7-008CFAC93D60.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/60E2170E-2A42-E811-BE2D-008CFAC94084.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/66A96172-2C42-E811-80E8-008CFAE45094.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/6CA65113-2A42-E811-84BB-008CFAC93DD8.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/76E4FB22-2342-E811-909E-008CFAC8CD50.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/889C4173-2C42-E811-A921-008CFAC942B4.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/8C96BD5D-2C42-E811-A6F2-008CFAC93B28.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/9207F2E1-2E42-E811-A176-008CFAEBDC04.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/96C7AFE2-2E42-E811-A575-008CFAC93DD8.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/9E7E8AAB-3542-E811-A0E1-008CFAC93F08.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/A6561C59-2542-E811-90CC-008CFAC93BF0.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/ACF66E61-3342-E811-905E-008CFAC94174.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/BA3999EC-3142-E811-A20C-008CFAE45060.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/C41D1A40-2442-E811-A089-008CFAC93EC0.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/CE42D852-9C42-E811-8838-008CFAC941C8.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/CEE44B20-2342-E811-BCE0-008CFAE45420.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/EAD607FA-2E42-E811-A30D-008CFAC93D1C.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/F60A3EFC-2942-E811-94D8-008CFAC91E98.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/F6EF5278-2C42-E811-834A-008CFA197AA0.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/06955664-3C42-E811-9B28-008CFAE45320.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/0AB1457F-3F42-E811-941D-008CFAEBDC04.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/0EB6BE38-4042-E811-91F1-008CFAEBDC90.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/18E293A6-4442-E811-985F-008CFAC9418C.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/1E69800D-3C42-E811-8FC9-008CFAC93C90.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/20A6255D-2B42-E811-AE6C-008CFAE45138.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/22F23A4D-3C42-E811-8992-008CFAED6FB8.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/2ED3488D-3D42-E811-96A0-008CFAEBDC04.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/32D4A56D-3C42-E811-9EA4-008CFAC918CC.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/3845C3D9-E141-E811-B580-008CFAC93CFC.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/3E16A98E-3D42-E811-9EDA-008CFAC94004.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/42837C64-3C42-E811-8812-008CFAC91A1C.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/4687AA54-3E42-E811-BF3D-008CFAED6D6C.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/4A1F340A-4542-E811-B56B-008CFA1974B4.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/4CE26A26-4142-E811-A6BD-008CFAC9403C.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/4E6192FE-3D42-E811-9A78-008CFAE45060.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/587D3320-3C42-E811-988C-008CFAC93C48.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/5C18E1FE-3D42-E811-8FFF-008CFAC93FF0.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/5EECCAFB-3A42-E811-AE5F-008CFAC93C0C.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/6C0F1228-4642-E811-9062-008CFAC942B4.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/9E1A4D07-4E42-E811-BE9E-008CFAE453F4.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/A07994FF-3E42-E811-9AFD-008CFAC91E24.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/BA38C4B7-EC41-E811-AF06-0025905A6066.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/BE9C92E3-3442-E811-982A-008CFAC917CC.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/D027C9BC-4142-E811-8414-008CFA1974B4.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/D664A83C-4042-E811-95D0-008CFAC941DC.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/DA517AA2-3F42-E811-866D-008CFAC91A1C.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/E22F2237-4042-E811-A5BE-008CFAC93C00.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/E44CF659-3E42-E811-B163-008CFAC93C50.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/EA188B07-3E42-E811-983D-008CFA11131C.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/EC40E98D-4342-E811-B354-008CFAC91D8C.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/F0BBA636-4042-E811-810E-008CFAC942A0.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/52A5775B-2742-E811-88E3-008CFAC93D60.root',
] )
