import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/02D7719D-01B5-E611-A239-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/049BBAC1-00B5-E611-86E2-5065F382C231.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/063A7239-FEB4-E611-8B13-5065F382C231.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/0C661EA3-FCB4-E611-ADC6-24BE05C616E1.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/12967DCC-FCB4-E611-AA02-4C79BA18183D.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/18A815D7-FBB4-E611-8675-002590488694.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/18C35CE3-00B5-E611-9248-0CC47A13CD44.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/1C20F377-01B5-E611-AAB4-5065F3816251.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/1E435379-02B5-E611-B8B1-5065F38182E1.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/2233659B-FDB4-E611-B54B-90B11C27F610.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/24930583-04B5-E611-87CF-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/249911DE-00B5-E611-BD49-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/2C610214-FBB4-E611-8151-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/2EE8902A-FFB4-E611-BD30-5065F38172A1.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/301D7E8C-F6B4-E611-AED9-5065F382C231.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/3413895A-19B5-E611-904F-A0369F3102F6.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/36F3C915-FAB4-E611-A51F-24BE05C616E1.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/3C73B0C9-FCB4-E611-A8A0-5065F38152E1.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/3E80F61B-19B5-E611-8345-0CC47AA989BA.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/48B08F6A-F7B4-E611-AE51-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/502563BF-01B5-E611-AA24-0CC47A13CCEE.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/50A551DE-00B5-E611-8B4A-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/5C61B396-19B5-E611-8E8D-ECF4BBE1BE18.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/5E5B2333-F8B4-E611-AFA3-A0369F30FFD2.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/5E81432C-FFB4-E611-B834-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/64498711-F9B4-E611-9DE3-24BE05CECB71.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/680CDF0D-FCB4-E611-9C11-24BE05C66892.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/688604C8-FCB4-E611-8C48-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/7280ACDE-FDB4-E611-AA06-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/72B8EFC8-FCB4-E611-B667-5065F3818271.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/76A5AADC-00B5-E611-B949-24BE05C616E1.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/7C50ADDD-00B5-E611-BE70-5065F381F1C1.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/7CFF9E30-F9B4-E611-9118-A0369F3102F6.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/7E05488C-F6B4-E611-9935-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/82099E98-F5B4-E611-A4C3-5065F37DC1B2.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/829BE019-FAB4-E611-9BB9-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/84609604-FCB4-E611-80EE-5065F37D8122.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/868B3A11-FBB4-E611-9591-5065F3816201.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/883D9DE1-FFB4-E611-964E-5065F38182E1.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/8856E011-FBB4-E611-92F9-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/8CCB51A4-00B5-E611-B483-5065F381E201.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/9294842B-FFB4-E611-85A2-24BE05CE2EC1.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/94B2CE9F-FDB4-E611-8F8F-5065F38182E1.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/9C2E1BFA-FFB4-E611-BFD2-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/A0560312-06B5-E611-BBEC-001E675A6725.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/A47C7DF4-06B5-E611-8B37-0CC47A13CCEE.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/A80CA897-F5B4-E611-A8F7-24BE05CEDCD1.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/A8F99C89-FEB4-E611-B199-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/ACFB392C-FFB4-E611-BA46-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/B0F86D23-FBB4-E611-9C25-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/B4F2C0DE-FDB4-E611-811E-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/B6C1EE43-08B5-E611-8627-0CC47AD98A9A.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/BC4F32BF-FBB4-E611-818B-5065F382C231.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/BC83F191-FEB4-E611-A4A9-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/BE8199DD-00B5-E611-960C-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/C0050ABD-02B5-E611-B7F3-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/C010268E-19B5-E611-B48E-001E677927CE.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/C471DE27-F9B4-E611-B658-5065F382C231.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/C8DE5FAD-FEB4-E611-A558-5065F3816251.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/CC24B71A-FFB4-E611-84D4-24BE05C616E1.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/D209B6CC-FEB4-E611-9310-0CC47A13D110.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/D2A9D809-FFB4-E611-905B-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/D4F517F3-FBB4-E611-A48E-5065F3816251.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/D8760D98-F5B4-E611-A915-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/DEBA684D-04B5-E611-9243-90B11C28232B.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/E21DA2FC-FFB4-E611-BDDA-0CC47AD99062.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/E61DE416-FAB4-E611-B9C2-24BE05C4D8C1.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/E6F1D55B-03B5-E611-BB2A-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/E6FD3E2C-FFB4-E611-9F05-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/EA63F524-FAB4-E611-BF75-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/EAEF17C0-FBB4-E611-B205-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/EE30E55A-FEB4-E611-BA72-5065F3818241.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/F060AE28-F9B4-E611-BF4E-5065F3816251.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/F6221D6A-03B5-E611-BE2F-0CC47AD98A9A.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/F66D922F-19B5-E611-9C70-B083FED16468.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/F6EA0538-F8B4-E611-820B-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/F87A17FB-FFB4-E611-94D8-5065F382C221.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/FAA69354-F7B4-E611-A9A8-A0369F3102B6.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/FAF41611-FBB4-E611-829F-5065F38182E1.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/FCCBC42B-FFB4-E611-B50A-A0000420FE80.root',
] )
