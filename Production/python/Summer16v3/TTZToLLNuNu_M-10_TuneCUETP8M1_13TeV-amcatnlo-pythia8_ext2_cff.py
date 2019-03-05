import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/00007F22-52CC-E811-AE41-0CC47AA53D8A.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/063E1F83-26D1-E811-8883-0025907D2430.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/06AFA1B4-EECF-E811-94AF-0CC47A0AD6C4.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/0C7C76A8-56CC-E811-893A-0CC47AA53D86.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/1203C39C-EECF-E811-97A8-0CC47AA53D8A.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/1464CFC8-5BCC-E811-A4AA-002590D9D894.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/16A11AF6-8DCE-E811-93CA-002590FD5A52.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/1A8A0E96-BECC-E811-8F10-0CC47AD24D28.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/20A0E836-64CC-E811-8B0D-002590D9D8B6.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/22E4FA2A-02CE-E811-B360-0025907DE278.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/30D478D2-58CC-E811-8EB8-0CC47AA53D7A.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/3225E476-06D0-E811-BC87-0025907E343C.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/3488DD7D-D1CC-E811-8149-00259075D72E.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/3632693E-EFCF-E811-8F7A-003048CB7B30.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/4054C57E-57CC-E811-881D-002590D9D8A4.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/4416060E-97CE-E811-B013-0CC47AA47914.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/446FF6A4-1FCF-E811-9C58-002590FD5A52.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/465EAA6B-A7CC-E811-A819-0CC47A0AD69E.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/468AFF04-07D0-E811-9F6C-003048CB860C.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/46C631F9-8ECC-E811-842C-002590D9D8A4.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/4CA4AC1E-EFCE-E811-AAE3-0CC47AA47914.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/50B80F80-EECF-E811-9E8C-0025901AC0F8.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/529C8590-58CC-E811-AC56-0CC47A57D086.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/6EBE5373-E9CE-E811-8DDA-00259075D708.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/724FEB15-45CC-E811-90D4-0CC47A0AD6AA.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/780E2D72-4BCC-E811-A431-0CC47AD24D28.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/82E66DFC-33CD-E811-A76A-002590785950.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/88A16B77-4BCC-E811-845A-0CC47A57CB8E.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/8A5EA0B4-EECF-E811-849F-0CC47A0AD6C4.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/8E3A3990-EFCF-E811-AEBA-0CC47A0AD476.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/986CC3D9-56CC-E811-8863-0CC47AB0B704.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/A01789F8-06D0-E811-9B46-00259019A43E.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/A21DF42B-34CF-E811-96E4-0CC47AA53D76.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/A6916E32-EFCF-E811-9A71-003048CB87DE.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/B67E5391-EFCF-E811-917D-00259075D702.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/BC2C8921-EECF-E811-84ED-0025907DE2A0.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/C40CC709-48CC-E811-9638-0CC47AA53D6A.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/D055C209-33CD-E811-9E2E-002590D9D984.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/D08495A9-06D0-E811-B33E-0CC47A0AD69E.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/D6482C0A-5DCC-E811-BD3F-00259029E920.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/DE64551F-B0D0-E811-8DB4-0025907DE278.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/E40D8722-5DCC-E811-BE17-0025901FB100.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/E43D8AF2-CCCC-E811-9CDB-0025907D24F0.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/E4D2786F-5ECC-E811-BE8B-00259019A418.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/E6E484C0-EECF-E811-B9B4-002590D9D984.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/EC484A9B-EECF-E811-ABFB-0CC47AA53D7A.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/EEA6B0FB-5CCC-E811-A05A-0025902BD8CE.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/F6997C13-47CC-E811-90CF-0CC47AD24CF8.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/FA8F79C0-F0CE-E811-88CC-0CC47A57CBCC.root',
] )