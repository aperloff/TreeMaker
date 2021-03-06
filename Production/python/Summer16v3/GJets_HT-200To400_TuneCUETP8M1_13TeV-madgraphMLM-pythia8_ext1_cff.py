import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/027B883A-9AEF-E811-ABA2-008CFA1C6414.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/06F9C7AF-4DF1-E811-9FD3-B4969109F230.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/0E28EA77-8DEF-E811-B748-008CFA110B10.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/1054489B-8DEF-E811-AA1B-008CFA56D764.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/106F5BAB-8BEF-E811-A524-A0369FD8FDB0.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/109563BF-99EF-E811-9BAF-008CFA197A70.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/10E55F0D-9BEF-E811-9849-008CFA1660F8.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/1846C066-96EF-E811-BA10-008CFA197FAC.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/24066D70-96EF-E811-80F6-008CFA1CB470.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/24504845-9CEF-E811-9811-008CFA197BBC.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/326FBCF1-99EF-E811-AE14-008CFA0F5040.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/3430DE83-91EF-E811-9364-B496910A8AC0.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/3C41781D-95EF-E811-A4BF-008CFA197A5C.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/4883B4F5-8CEF-E811-880A-008CFA5807F0.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/48EE8E3C-8DEF-E811-AC8B-B4969109F628.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/54C73FF0-93EF-E811-999A-008CFA1C6414.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/54D57351-9BEF-E811-A6D9-008CFA111200.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/54FBEF74-94EF-E811-9763-008CFA198258.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/5AAF369A-96EF-E811-A75F-008CFA1CBB34.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/5ACB2124-8DEF-E811-8386-B496910A0430.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/60283B76-91EF-E811-81F5-008CFA0A58B4.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/602907C3-4DF1-E811-BC42-008CFA0A5808.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/62039F9C-8EEF-E811-94BF-B4969109FDE0.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/62165920-93EF-E811-8F57-008CFA197EB0.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/640FBD9C-8FEF-E811-AE6A-B496910A80EC.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/647C3E99-8BEF-E811-8B0C-A0369FC5E8FC.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/7025526A-8DEF-E811-8B44-008CFA064778.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/70CAF20C-8CEF-E811-AA6D-549F35AF4488.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/727502AB-C2EF-E811-A321-A0369FC5DCC0.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/80AF8C68-92EF-E811-8B20-008CFA1C6564.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/80E13220-94EF-E811-9750-00266CFCCBFC.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/86338640-8CEF-E811-ACBB-A0369FC5EE94.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/864EF7B4-4DF1-E811-B83E-008CFA1C6458.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/88D51BB2-4DF1-E811-A3D8-A0369FC5E71C.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/8ED1D23B-8FEF-E811-B89E-A0369FC5E22C.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/92BD9037-9AEF-E811-855E-B4969109F628.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/94C133FC-8BEF-E811-A1C6-549F35AC7DEE.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/96C5F3B3-4DF1-E811-8320-549F358EB7D7.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/98BED43C-BDEF-E811-A71F-008CFA197A70.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/9CB5F1F0-CDEF-E811-9E36-B496910A0430.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/A0E4F82E-8DEF-E811-A292-00266CFCC490.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/A0F667AF-4DF1-E811-A4D3-B496910A9A40.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/A0FA7457-91EF-E811-B68E-B496910A0554.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/A6511BA5-90EF-E811-AE2B-008CFA197C38.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/A668614F-93EF-E811-A551-00266CFCC490.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/AAE6B7A4-92EF-E811-8177-B496910A80F0.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/AED6401B-90EF-E811-8132-008CFA1CBA7C.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/B253DBB4-94EF-E811-81A8-008CFA197D38.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/B875A2A9-8DEF-E811-9348-A0369FC5DF9C.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/BED52809-92EF-E811-8859-549F35AF4517.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/C46D8C8E-92EF-E811-852D-008CFA152144.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/C8208866-94EF-E811-A108-A0369FC5B4F4.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/C880D3D5-8DEF-E811-8120-B496910A8AC0.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/CA7F6D04-92EF-E811-B69E-008CFA198314.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/CAC3DFD1-8BEF-E811-926D-A0369FC5E49C.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/CCCBCDF8-E4EF-E811-A0F5-A0369FC4C930.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/CEC27A61-95EF-E811-85A8-008CFA197B44.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/D20FEA94-8DEF-E811-A1EF-008CFA197C38.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/D25DCAC9-8EEF-E811-9DDD-549F35AD8BD6.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/DA8988CD-98EF-E811-A3DA-A0369FC5B7E0.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/DE5F0052-95EF-E811-848E-008CFA0A570C.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/E007F0AD-4DF1-E811-94D6-B496910A85E4.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/E0081D60-92EF-E811-9680-549F35AC7E08.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/E25E46F0-94EF-E811-8234-A0369FC4C930.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/E2C8907A-9CEF-E811-AFC9-008CFA197D98.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/E4791008-91EF-E811-9234-008CFA1CB740.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/E8EC6D81-93EF-E811-846E-008CFA197FAC.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/F09DDB3F-90EF-E811-BEB7-A0369FC5E71C.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/F2E6DB85-9AEF-E811-845B-A0369F7FC5BC.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/169FBD28-01F1-E811-BEB8-008CFA197D98.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/260B1CFC-EEF0-E811-829F-B4969109F68C.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/26EF5FDF-F7F0-E811-88DC-A0369FC52630.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/32D2926C-D5F0-E811-9C27-B496910A041C.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/4497B70E-ECF0-E811-A3A6-A0369FC5B7B0.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/4A5A52A9-D4F0-E811-BFC4-A0369FC52630.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/7699C1D1-E5F0-E811-954E-B4969109FE30.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/A4168F4F-E5F0-E811-90A5-008CFA1CB73C.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/B68BDAC3-B7F0-E811-8765-B496910A041C.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/BCB77039-F7F0-E811-BEA4-A0369FC5DCBC.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/C841B3BA-CFF0-E811-83D3-A0369FC51AE4.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/CC1F199F-B7F0-E811-A967-008CFA1CB73C.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/CC61AC74-D5F0-E811-8513-A0369F7FC0BC.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/E439E254-D4F0-E811-A287-008CFA1983BC.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/EC56CC6A-94F2-E811-A0DC-A0369FD8FDB0.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/FC873C53-FCF0-E811-8D55-549F35AC7E08.root',
] )
