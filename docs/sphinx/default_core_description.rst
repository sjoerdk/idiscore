.. _default_core_description:

=============================
IDISCore instance description
=============================

idiscore lib version: 0.3.1


Bouncers:
=========

* Reject encapsulated PDF and CDA
* Reject non-standard DICOM types by SOPClassUID


Profile 'idiscore default profile'
==================================

Rule sets:
----------

* Basic Application Level Confidentiality Profile
* Clean Descriptors Option
* Retain Patient Characteristics Option
* Retain Device Identity Option
* Retain Safe Private Option


All rules, alphabetically:
--------------------------

* AccessionNumber - (0008, 0050) - Empty
* AcquisitionComments - (0018, 4000) - Clean
* AcquisitionContextSequence - (0040, 0555) - Remove
* AcquisitionDate - (0008, 0022) - Remove
* AcquisitionDateTime - (0008, 002a) - Remove
* AcquisitionDeviceProcessingDescription - (0018, 1400) - Clean
* AcquisitionProtocolDescription - (0018, 9424) - Clean
* AcquisitionTime - (0008, 0032) - Remove
* ActualHumanPerformersSequence - (0040, 4035) - Remove
* AdditionalPatientHistory - (0010, 21b0) - Clean
* AddressTrial - (0040, a353) - Remove
* AdmissionID - (0038, 0010) - Remove
* AdmittingDate - (0038, 0020) - Remove
* AdmittingDiagnosesCodeSequence - (0008, 1084) - Clean
* AdmittingDiagnosesDescription - (0008, 1080) - Clean
* AdmittingTime - (0038, 0021) - Remove
* AffectedSOPInstanceUID - (0000, 1000) - Remove
* Allergies - (0010, 2110) - Clean
* Arbitrary - (4000, 0010) - Remove
* AuthorObserverSequence - (0040, a078) - Remove
* BarcodeValue - (2200, 0005) - Remove
* BeamDescription - (300a, 00c3) - Clean
* BolusDescription - (300a, 00dd) - Clean
* BranchOfService - (0010, 1081) - Remove
* CameraOwnerName - (0016, 004d) - Remove
* CassetteID - (0018, 1007) - Keep
* ClinicalTrialCoordinatingCenterName - (0012, 0060) - Empty
* ClinicalTrialProtocolEthicsCommitteeApprovalNumber - (0012, 0082) - Remove
* ClinicalTrialProtocolEthicsCommitteeName - (0012, 0081) - Replace
* ClinicalTrialProtocolID - (0012, 0020) - Replace
* ClinicalTrialProtocolName - (0012, 0021) - Empty
* ClinicalTrialSeriesDescription - (0012, 0072) - Clean
* ClinicalTrialSeriesID - (0012, 0071) - Remove
* ClinicalTrialSiteID - (0012, 0030) - Empty
* ClinicalTrialSiteName - (0012, 0031) - Empty
* ClinicalTrialSponsorName - (0012, 0010) - Replace
* ClinicalTrialSubjectID - (0012, 0040) - Replace
* ClinicalTrialSubjectReadingID - (0012, 0042) - Replace
* ClinicalTrialTimePointDescription - (0012, 0051) - Clean
* ClinicalTrialTimePointID - (0012, 0050) - Empty
* CommentsOnThePerformedProcedureStep - (0040, 0280) - Clean
* CompensatorDescription - (300a, 02eb) - Clean
* ConcatenationUID - (0020, 9161) - HashUID
* ConceptualVolumeCombinationDescription - (3010, 000f) - Clean
* ConceptualVolumeDescription - (3010, 0017) - Clean
* ConceptualVolumeUID - (3010, 0006) - HashUID
* ConfidentialityConstraintOnPatientDataDescription - (0040, 3001) - Remove
* ConstituentConceptualVolumeUID - (3010, 0013) - HashUID
* ConsultingPhysicianIdentificationSequence - (0008, 009d) - Remove
* ConsultingPhysicianName - (0008, 009c) - Empty
* ContainerComponentID - (0050, 001b) - Remove
* ContainerDescription - (0040, 051a) - Clean
* ContainerIdentifier - (0040, 0512) - Replace
* ContentCreatorIdentificationCodeSequence - (0070, 0086) - Remove
* ContentCreatorName - (0070, 0084) - Replace
* ContentDate - (0008, 0023) - Replace
* ContentSequence - (0040, a730) - Replace
* ContentTime - (0008, 0033) - Replace
* ContrastBolusAgent - (0018, 0010) - Clean
* ContributionDescription - (0018, a003) - Clean
* CountryOfResidence - (0010, 2150) - Remove
* CurrentObserverTrial - (0040, a307) - Remove
* CurrentPatientLocation - (0038, 0300) - Remove
* CurveDate - (0008, 0025) - Remove
* CurveTime - (0008, 0035) - Remove
* CustodialOrganizationSequence - (0040, a07c) - Remove
* DataSetTrailingPadding - (fffc, fffc) - Remove
* DecompositionDescription - (0018, 937f) - Clean
* DerivationDescription - (0008, 2111) - Clean
* DetectorID - (0018, 700a) - Keep
* DeviceAlternateIdentifier - (3010, 001b) - Empty
* DeviceDescription - (0050, 0020) - Keep
* DeviceLabel - (3010, 002d) - Keep
* DeviceSerialNumber - (0018, 1000) - Keep
* DeviceSettingDescription - (0016, 004b) - Clean
* DeviceUID - (0018, 1002) - Keep
* DigitalSignatureUID - (0400, 0100) - HashUID
* DigitalSignaturesSequence - (fffa, fffa) - Remove
* DimensionOrganizationUID - (0020, 9164) - HashUID
* DischargeDiagnosisDescription - (0038, 0040) - Clean
* DistributionAddress - (4008, 011a) - Remove
* DistributionName - (4008, 0119) - Remove
* DoseReferenceDescription - (300a, 0016) - Clean
* DoseReferenceUID - (300a, 0013) - HashUID
* DosimetricObjectiveUID - (3010, 006e) - HashUID
* EndAcquisitionDateTime - (0018, 9517) - Remove
* EntityDescription - (3010, 0037) - Clean
* EntityLabel - (3010, 0035) - Clean
* EntityLongLabel - (3010, 0038) - Clean
* EntityName - (3010, 0036) - Clean
* EquipmentFrameOfReferenceDescription - (300a, 0676) - Clean
* EthnicGroup - (0010, 2160) - Keep
* ExpectedCompletionDateTime - (0040, 4011) - Remove
* FailedSOPInstanceUIDList - (0008, 0058) - HashUID
* FiducialUID - (0070, 031a) - HashUID
* FillerOrderNumberImagingServiceRequest - (0040, 2017) - Empty
* FirstTreatmentDate - (3008, 0054) - Remove
* FixationDeviceDescription - (300a, 0196) - Clean
* FlowIdentifier - (0034, 0002) - Replace
* FlowIdentifierSequence - (0034, 0001) - Replace
* FractionGroupDescription - (300a, 0072) - Clean
* FractionationNotes - (3010, 007f) - Clean
* FrameComments - (0020, 9158) - Clean
* FrameOfReferenceUID - (0020, 0052) - HashUID
* FrameOriginTimestamp - (0034, 0007) - Replace
* GPSAltitude - (0016, 0076) - Remove
* GPSAltitudeRef - (0016, 0075) - Remove
* GPSAreaInformation - (0016, 008c) - Remove
* GPSDOP - (0016, 007b) - Remove
* GPSDateStamp - (0016, 008d) - Remove
* GPSDestBearing - (0016, 0088) - Remove
* GPSDestBearingRef - (0016, 0087) - Remove
* GPSDestDistance - (0016, 008a) - Remove
* GPSDestDistanceRef - (0016, 0089) - Remove
* GPSDestLatitude - (0016, 0084) - Remove
* GPSDestLatitudeRef - (0016, 0083) - Remove
* GPSDestLongitude - (0016, 0086) - Remove
* GPSDestLongitudeRef - (0016, 0085) - Remove
* GPSDifferential - (0016, 008e) - Remove
* GPSImgDirection - (0016, 0081) - Remove
* GPSImgDirectionRef - (0016, 0080) - Remove
* GPSLatitude - (0016, 0072) - Remove
* GPSLatitudeRef - (0016, 0071) - Remove
* GPSLongitude - (0016, 0074) - Remove
* GPSLongitudeRef - (0016, 0073) - Remove
* GPSMapDatum - (0016, 0082) - Remove
* GPSMeasureMode - (0016, 007a) - Remove
* GPSProcessingMethod - (0016, 008b) - Remove
* GPSSatellites - (0016, 0078) - Remove
* GPSSpeed - (0016, 007d) - Remove
* GPSSpeedRef - (0016, 007c) - Remove
* GPSStatus - (0016, 0079) - Remove
* GPSTimeStamp - (0016, 0077) - Remove
* GPSTrack - (0016, 007f) - Remove
* GPSTrackRef - (0016, 007e) - Remove
* GPSVersionID - (0016, 0070) - Remove
* GantryID - (0018, 1008) - Keep
* GeneratorID - (0018, 1005) - Keep
* GraphicAnnotationSequence - (0070, 0001) - Replace
* HumanPerformerName - (0040, 4037) - Remove
* HumanPerformerOrganization - (0040, 4036) - Remove
* IconImageSequence - (0088, 0200) - Remove
* IdentifyingComments - (0008, 4000) - Clean
* ImageComments - (0020, 4000) - Clean
* ImagePresentationComments - (0028, 4000) - Remove
* ImagingServiceRequestComments - (0040, 2400) - Clean
* Impressions - (4008, 0300) - Clean
* InstanceCoercionDateTime - (0008, 0015) - Remove
* InstanceCreatorUID - (0008, 0014) - HashUID
* InstanceOriginStatus - (0400, 0600) - Remove
* InstitutionAddress - (0008, 0081) - Remove
* InstitutionCodeSequence - (0008, 0082) - Remove
* InstitutionName - (0008, 0080) - Remove
* InstitutionalDepartmentName - (0008, 1040) - Remove
* InstitutionalDepartmentTypeCodeSequence - (0008, 1041) - Remove
* InsurancePlanIdentification - (0010, 1050) - Remove
* IntendedPhaseEndDate - (3010, 004d) - Remove
* IntendedPhaseStartDate - (3010, 004c) - Remove
* IntendedRecipientsOfResultsIdentificationSequence - (0040, 1011) - Remove
* InterpretationApproverSequence - (4008, 0111) - Remove
* InterpretationAuthor - (4008, 010c) - Remove
* InterpretationDiagnosisDescription - (4008, 0115) - Clean
* InterpretationIDIssuer - (4008, 0202) - Remove
* InterpretationRecorder - (4008, 0102) - Remove
* InterpretationText - (4008, 010b) - Clean
* InterpretationTranscriber - (4008, 010a) - Remove
* IrradiationEventUID - (0008, 3010) - HashUID
* IssuerOfAdmissionID - (0038, 0011) - Remove
* IssuerOfAdmissionIDSequence - (0038, 0014) - Remove
* IssuerOfPatientID - (0010, 0021) - Remove
* IssuerOfServiceEpisodeID - (0038, 0061) - Remove
* IssuerOfServiceEpisodeIDSequence - (0038, 0064) - Remove
* IssuerOfTheContainerIdentifierSequence - (0040, 0513) - Empty
* IssuerOfTheSpecimenIdentifierSequence - (0040, 0562) - Empty
* LabelText - (2200, 0002) - Clean
* LargePaletteColorLookupTableUID - (0028, 1214) - HashUID
* LastMenstrualDate - (0010, 21d0) - Remove
* LensMake - (0016, 004f) - Keep
* LensModel - (0016, 0050) - Keep
* LensSerialNumber - (0016, 0051) - Keep
* LensSpecification - (0016, 004e) - Keep
* LongDeviceDescription - (0050, 0021) - Clean
* MAC - (0400, 0404) - Remove
* MakerNote - (0016, 002b) - Clean
* ManufacturerDeviceClassUID - (0018, 100b) - Keep
* ManufacturerDeviceIdentifier - (3010, 0043) - Keep
* MediaStorageSOPInstanceUID - (0002, 0003) - HashUID
* MedicalAlerts - (0010, 2000) - Clean
* MedicalRecordLocator - (0010, 1090) - Remove
* MilitaryRank - (0010, 1080) - Remove
* ModifiedAttributesSequence - (0400, 0550) - Remove
* ModifiedImageDescription - (0020, 3406) - Remove
* ModifyingDeviceID - (0020, 3401) - Remove
* MostRecentTreatmentDate - (3008, 0056) - Remove
* MultienergyAcquisitionDescription - (0018, 937b) - Clean
* NameOfPhysiciansReadingStudy - (0008, 1060) - Remove
* NamesOfIntendedRecipientsOfResults - (0040, 1010) - Remove
* ObservationDateTrial - (0040, a192) - Remove
* ObservationSubjectUIDTrial - (0040, a402) - HashUID
* ObservationTimeTrial - (0040, a193) - Remove
* ObservationUID - (0040, a171) - HashUID
* Occupation - (0010, 2180) - Clean
* OperatorIdentificationSequence - (0008, 1072) - Remove
* OperatorsName - (0008, 1070) - Remove
* OrderCallbackPhoneNumber - (0040, 2010) - Remove
* OrderCallbackTelecomInformation - (0040, 2011) - Remove
* OrderEnteredBy - (0040, 2008) - Remove
* OrderEntererLocation - (0040, 2009) - Remove
* OriginalAttributesSequence - (0400, 0561) - Remove
* OtherPatientIDs - (0010, 1000) - Remove
* OtherPatientIDsSequence - (0010, 1002) - Remove
* OtherPatientNames - (0010, 1001) - Remove
* OverlayComments - (60xx, 4000) - Remove
* OverlayData - (60xx, 3000) - Remove
* OverlayDate - (0008, 0024) - Remove
* OverlayTime - (0008, 0034) - Remove
* PaletteColorLookupTableUID - (0028, 1199) - HashUID
* ParticipantSequence - (0040, a07a) - Remove
* PatientAddress - (0010, 1040) - Remove
* PatientAge - (0010, 1010) - Keep
* PatientBirthDate - (0010, 0030) - Empty
* PatientBirthName - (0010, 1005) - Remove
* PatientBirthTime - (0010, 0032) - Remove
* PatientComments - (0010, 4000) - Clean
* PatientID - (0010, 0020) - Empty
* PatientInstitutionResidence - (0038, 0400) - Remove
* PatientInsurancePlanCodeSequence - (0010, 0050) - Remove
* PatientMotherBirthName - (0010, 1060) - Remove
* PatientName - (0010, 0010) - Empty
* PatientPrimaryLanguageCodeSequence - (0010, 0101) - Remove
* PatientPrimaryLanguageModifierCodeSequence - (0010, 0102) - Remove
* PatientReligiousPreference - (0010, 21f0) - Remove
* PatientSetupUID - (300a, 0650) - HashUID
* PatientSex - (0010, 0040) - Keep
* PatientSexNeutered - (0010, 2203) - Keep
* PatientSize - (0010, 1020) - Keep
* PatientState - (0038, 0500) - Clean
* PatientTelecomInformation - (0010, 2155) - Remove
* PatientTelephoneNumbers - (0010, 2154) - Remove
* PatientTransportArrangements - (0040, 1004) - Remove
* PatientWeight - (0010, 1030) - Keep
* PerformedLocation - (0040, 0243) - Remove
* PerformedProcedureStepDescription - (0040, 0254) - Clean
* PerformedProcedureStepEndDate - (0040, 0250) - Remove
* PerformedProcedureStepEndDateTime - (0040, 4051) - Remove
* PerformedProcedureStepEndTime - (0040, 0251) - Remove
* PerformedProcedureStepID - (0040, 0253) - Remove
* PerformedProcedureStepStartDate - (0040, 0244) - Remove
* PerformedProcedureStepStartDateTime - (0040, 4050) - Remove
* PerformedProcedureStepStartTime - (0040, 0245) - Remove
* PerformedStationAETitle - (0040, 0241) - Keep
* PerformedStationGeographicLocationCodeSequence - (0040, 4030) - Keep
* PerformedStationName - (0040, 0242) - Keep
* PerformedStationNameCodeSequence - (0040, 4028) - Keep
* PerformingPhysicianIdentificationSequence - (0008, 1052) - Remove
* PerformingPhysicianName - (0008, 1050) - Remove
* PersonAddress - (0040, 1102) - Remove
* PersonIdentificationCodeSequence - (0040, 1101) - Replace
* PersonName - (0040, a123) - Replace
* PersonTelecomInformation - (0040, 1104) - Remove
* PersonTelephoneNumbers - (0040, 1103) - Remove
* PhysicianApprovingInterpretation - (4008, 0114) - Remove
* PhysiciansOfRecord - (0008, 1048) - Remove
* PhysiciansOfRecordIdentificationSequence - (0008, 1049) - Remove
* PhysiciansReadingStudyIdentificationSequence - (0008, 1062) - Remove
* PlacerOrderNumberImagingServiceRequest - (0040, 2016) - Empty
* PlateID - (0018, 1004) - Keep
* PreMedication - (0040, 0012) - Clean
* PregnancyStatus - (0010, 21c0) - Keep
* PrescriptionDescription - (300a, 000e) - Clean
* PrescriptionNotes - (3010, 007b) - Clean
* PrescriptionNotesSequence - (3010, 0081) - Clean
* PresentationDisplayCollectionUID - (0070, 1101) - HashUID
* PresentationSequenceCollectionUID - (0070, 1102) - HashUID
* PriorTreatmentDoseDescription - (3010, 0061) - Clean
* Private Attributes - PrivateAttributes - Clean
* ProcedureStepCancellationDateTime - (0040, 4052) - Remove
* ProtocolName - (0018, 1030) - Clean
* RTAccessoryDeviceSlotID - (300a, 0615) - Empty
* RTAccessoryHolderSlotID - (300a, 0611) - Empty
* RTPhysicianIntentNarrative - (3010, 005a) - Clean
* RTPlanDate - (300a, 0006) - Remove
* RTPlanDescription - (300a, 0004) - Clean
* RTPlanLabel - (300a, 0002) - Clean
* RTPlanName - (300a, 0003) - Clean
* RTPlanTime - (300a, 0007) - Remove
* RTPrescriptionLabel - (3010, 0054) - Clean
* RTToleranceSetLabel - (300a, 062a) - Clean
* RTTreatmentApproachLabel - (3010, 0056) - Clean
* RTTreatmentPhaseUID - (3010, 003b) - HashUID
* RadiationDoseIdentificationLabel - (300a, 0619) - Clean
* RadiationDoseInVivoMeasurementLabel - (300a, 0623) - Clean
* RadiationGenerationModeDescription - (300a, 067d) - Clean
* RadiationGenerationModeLabel - (300a, 067c) - Clean
* ReasonForOmissionDescription - (300c, 0113) - Clean
* ReasonForRequestedProcedureCodeSequence - (0040, 100a) - Clean
* ReasonForStudy - (0032, 1030) - Clean
* ReasonForSuperseding - (3010, 005c) - Clean
* ReasonForTheImagingServiceRequest - (0040, 2001) - Clean
* ReasonForTheRequestedProcedure - (0040, 1002) - Clean
* ReasonForVisit - (0032, 1066) - Clean
* ReasonForVisitCodeSequence - (0032, 1067) - Clean
* ReferencedConceptualVolumeUID - (3010, 000b) - HashUID
* ReferencedDigitalSignatureSequence - (0400, 0402) - Remove
* ReferencedDoseReferenceUID - (300a, 0083) - HashUID
* ReferencedDosimetricObjectiveUID - (3010, 006f) - HashUID
* ReferencedFiducialsUID - (3010, 0031) - HashUID
* ReferencedFrameOfReferenceUID - (3006, 0024) - HashUID
* ReferencedGeneralPurposeScheduledProcedureStepTransactionUID - (0040, 4023) - HashUID
* ReferencedImageSequence - (0008, 1140) - Remove
* ReferencedObservationUIDTrial - (0040, a172) - HashUID
* ReferencedPatientAliasSequence - (0038, 0004) - Remove
* ReferencedPatientPhotoSequence - (0010, 1100) - Remove
* ReferencedPatientSequence - (0008, 1120) - Remove
* ReferencedPerformedProcedureStepSequence - (0008, 1111) - Remove
* ReferencedSOPInstanceMACSequence - (0400, 0403) - Remove
* ReferencedSOPInstanceUID - (0008, 1155) - HashUID
* ReferencedSOPInstanceUIDInFile - (0004, 1511) - HashUID
* ReferencedStudySequence - (0008, 1110) - Remove
* ReferringPhysicianAddress - (0008, 0092) - Remove
* ReferringPhysicianIdentificationSequence - (0008, 0096) - Remove
* ReferringPhysicianName - (0008, 0090) - Empty
* ReferringPhysicianTelephoneNumbers - (0008, 0094) - Remove
* RegionOfResidence - (0010, 2152) - Remove
* RelatedFrameOfReferenceUID - (3006, 00c2) - HashUID
* RequestAttributesSequence - (0040, 0275) - Clean
* RequestedContrastAgent - (0032, 1070) - Clean
* RequestedProcedureComments - (0040, 1400) - Clean
* RequestedProcedureDescription - (0032, 1060) - Clean
* RequestedProcedureID - (0040, 1001) - Remove
* RequestedProcedureLocation - (0040, 1005) - Remove
* RequestedSOPInstanceUID - (0000, 1001) - HashUID
* RequestingPhysician - (0032, 1032) - Remove
* RequestingService - (0032, 1033) - Remove
* RespiratoryMotionCompensationTechniqueDescription - (0018, 9185) - Clean
* ResponsibleOrganization - (0010, 2299) - Remove
* ResponsiblePerson - (0010, 2297) - Remove
* ResultsComments - (4008, 4000) - Clean
* ResultsDistributionListSequence - (4008, 0118) - Remove
* ResultsIDIssuer - (4008, 0042) - Remove
* ReviewerName - (300e, 0008) - Remove
* SOPInstanceUID - (0008, 0018) - HashUID
* ScheduledHumanPerformersSequence - (0040, 4034) - Remove
* ScheduledPatientInstitutionResidence - (0038, 001e) - Remove
* ScheduledPerformingPhysicianIdentificationSequence - (0040, 000b) - Remove
* ScheduledPerformingPhysicianName - (0040, 0006) - Remove
* ScheduledProcedureStepDescription - (0040, 0007) - Clean
* ScheduledProcedureStepEndDate - (0040, 0004) - Remove
* ScheduledProcedureStepEndTime - (0040, 0005) - Remove
* ScheduledProcedureStepExpirationDateTime - (0040, 4008) - Remove
* ScheduledProcedureStepLocation - (0040, 0011) - Keep
* ScheduledProcedureStepModificationDateTime - (0040, 4010) - Remove
* ScheduledProcedureStepStartDate - (0040, 0002) - Remove
* ScheduledProcedureStepStartDateTime - (0040, 4005) - Remove
* ScheduledProcedureStepStartTime - (0040, 0003) - Remove
* ScheduledStationAETitle - (0040, 0001) - Keep
* ScheduledStationGeographicLocationCodeSequence - (0040, 4027) - Keep
* ScheduledStationName - (0040, 0010) - Keep
* ScheduledStationNameCodeSequence - (0040, 4025) - Keep
* ScheduledStudyLocation - (0032, 1020) - Keep
* ScheduledStudyLocationAETitle - (0032, 1021) - Keep
* SeriesDate - (0008, 0021) - Remove
* SeriesDescription - (0008, 103e) - Clean
* SeriesInstanceUID - (0020, 000e) - HashUID
* SeriesTime - (0008, 0031) - Remove
* ServiceEpisodeDescription - (0038, 0062) - Clean
* ServiceEpisodeID - (0038, 0060) - Remove
* SetupTechniqueDescription - (300a, 01b2) - Clean
* ShieldingDeviceDescription - (300a, 01a6) - Clean
* SlideIdentifier - (0040, 06fa) - Remove
* SmokingStatus - (0010, 21a0) - Keep
* SourceConceptualVolumeUID - (3010, 0015) - HashUID
* SourceEndDateTime - (0018, 936a) - Replace
* SourceIdentifier - (0034, 0005) - Replace
* SourceImageSequence - (0008, 2112) - Remove
* SourceManufacturer - (300a, 0216) - Keep
* SourceSerialNumber - (3008, 0105) - Keep
* SourceStartDateTime - (0018, 9369) - Replace
* SpecialNeeds - (0038, 0050) - Clean
* SpecimenAccessionNumber - (0040, 050a) - Remove
* SpecimenDetailedDescription - (0040, 0602) - Clean
* SpecimenIdentifier - (0040, 0551) - Replace
* SpecimenPreparationSequence - (0040, 0610) - Empty
* SpecimenShortDescription - (0040, 0600) - Clean
* SpecimenUID - (0040, 0554) - HashUID
* StartAcquisitionDateTime - (0018, 9516) - Remove
* StationName - (0008, 1010) - Keep
* StorageMediaFileSetUID - (0088, 0140) - HashUID
* StudyComments - (0032, 4000) - Clean
* StudyDate - (0008, 0020) - Empty
* StudyDescription - (0008, 1030) - Clean
* StudyID - (0020, 0010) - Empty
* StudyIDIssuer - (0032, 0012) - Remove
* StudyInstanceUID - (0020, 000d) - HashUID
* StudyTime - (0008, 0030) - Empty
* SynchronizationFrameOfReferenceUID - (0020, 0200) - HashUID
* TargetUID - (0018, 2042) - HashUID
* TelephoneNumberTrial - (0040, a354) - Remove
* TemplateExtensionCreatorUID - (0040, db0d) - HashUID
* TemplateExtensionOrganizationUID - (0040, db0c) - HashUID
* TextComments - (4000, 4000) - Remove
* TextString - (2030, 0020) - Remove
* TimezoneOffsetFromUTC - (0008, 0201) - Remove
* TopicAuthor - (0088, 0910) - Remove
* TopicKeywords - (0088, 0912) - Remove
* TopicSubject - (0088, 0906) - Remove
* TopicTitle - (0088, 0904) - Remove
* TrackingUID - (0062, 0021) - HashUID
* TransactionUID - (0008, 1195) - HashUID
* TreatmentDate - (3008, 0250) - Remove
* TreatmentMachineName - (300a, 00b2) - Keep
* TreatmentPositionGroupLabel - (300a, 0608) - Clean
* TreatmentPositionGroupUID - (300a, 0609) - HashUID
* TreatmentSite - (3010, 0077) - Clean
* TreatmentTechniqueNotes - (3010, 007a) - Clean
* TreatmentTime - (3008, 0251) - Remove
* UDISequence - (0018, 100a) - Keep
* UID - (0040, a124) - HashUID
* UniqueDeviceIdentifier - (0018, 1009) - Keep
* Unknown Repeater tag 50xxxxxx - (50xx, xxxx) - Remove
* Unknown Tag - (003a, 0310) - HashUID
* Unknown Tag - (003a, 0314) - Replace
* Unknown Tag - (300a, 0700) - HashUID
* Unknown Tag - (300a, 0734) - Clean
* Unknown Tag - (300a, 0736) - Replace
* Unknown Tag - (300a, 073a) - Replace
* Unknown Tag - (300a, 0741) - Replace
* Unknown Tag - (300a, 0742) - Clean
* Unknown Tag - (300a, 0760) - Replace
* Unknown Tag - (300a, 0783) - Clean
* UserContentLabel - (3010, 0033) - Clean
* UserContentLongLabel - (3010, 0034) - Clean
* VerbalSourceIdentifierCodeSequenceTrial - (0040, a358) - Remove
* VerbalSourceTrial - (0040, a352) - Remove
* VerifyingObserverIdentificationCodeSequence - (0040, a088) - Empty
* VerifyingObserverName - (0040, a075) - Replace
* VerifyingObserverSequence - (0040, a073) - Replace
* VerifyingOrganization - (0040, a027) - Replace
* VisitComments - (0038, 4000) - Clean
* XRayDetectorID - (0018, 9371) - Keep
* XRayDetectorLabel - (0018, 9373) - Keep
* XRaySourceID - (0018, 9367) - Keep


All rules, by tag:
------------------

* (0000, 1000) (AffectedSOPInstanceUID) - Remove
* (0000, 1001) (RequestedSOPInstanceUID) - HashUID
* (0002, 0003) (MediaStorageSOPInstanceUID) - HashUID
* (0004, 1511) (ReferencedSOPInstanceUIDInFile) - HashUID
* (0008, 0014) (InstanceCreatorUID) - HashUID
* (0008, 0015) (InstanceCoercionDateTime) - Remove
* (0008, 0018) (SOPInstanceUID) - HashUID
* (0008, 0020) (StudyDate) - Empty
* (0008, 0021) (SeriesDate) - Remove
* (0008, 0022) (AcquisitionDate) - Remove
* (0008, 0023) (ContentDate) - Replace
* (0008, 0024) (OverlayDate) - Remove
* (0008, 0025) (CurveDate) - Remove
* (0008, 002a) (AcquisitionDateTime) - Remove
* (0008, 0030) (StudyTime) - Empty
* (0008, 0031) (SeriesTime) - Remove
* (0008, 0032) (AcquisitionTime) - Remove
* (0008, 0033) (ContentTime) - Replace
* (0008, 0034) (OverlayTime) - Remove
* (0008, 0035) (CurveTime) - Remove
* (0008, 0050) (AccessionNumber) - Empty
* (0008, 0058) (FailedSOPInstanceUIDList) - HashUID
* (0008, 0080) (InstitutionName) - Remove
* (0008, 0081) (InstitutionAddress) - Remove
* (0008, 0082) (InstitutionCodeSequence) - Remove
* (0008, 0090) (ReferringPhysicianName) - Empty
* (0008, 0092) (ReferringPhysicianAddress) - Remove
* (0008, 0094) (ReferringPhysicianTelephoneNumbers) - Remove
* (0008, 0096) (ReferringPhysicianIdentificationSequence) - Remove
* (0008, 009c) (ConsultingPhysicianName) - Empty
* (0008, 009d) (ConsultingPhysicianIdentificationSequence) - Remove
* (0008, 0201) (TimezoneOffsetFromUTC) - Remove
* (0008, 1010) (StationName) - Keep
* (0008, 1030) (StudyDescription) - Clean
* (0008, 103e) (SeriesDescription) - Clean
* (0008, 1040) (InstitutionalDepartmentName) - Remove
* (0008, 1041) (InstitutionalDepartmentTypeCodeSequence) - Remove
* (0008, 1048) (PhysiciansOfRecord) - Remove
* (0008, 1049) (PhysiciansOfRecordIdentificationSequence) - Remove
* (0008, 1050) (PerformingPhysicianName) - Remove
* (0008, 1052) (PerformingPhysicianIdentificationSequence) - Remove
* (0008, 1060) (NameOfPhysiciansReadingStudy) - Remove
* (0008, 1062) (PhysiciansReadingStudyIdentificationSequence) - Remove
* (0008, 1070) (OperatorsName) - Remove
* (0008, 1072) (OperatorIdentificationSequence) - Remove
* (0008, 1080) (AdmittingDiagnosesDescription) - Clean
* (0008, 1084) (AdmittingDiagnosesCodeSequence) - Clean
* (0008, 1110) (ReferencedStudySequence) - Remove
* (0008, 1111) (ReferencedPerformedProcedureStepSequence) - Remove
* (0008, 1120) (ReferencedPatientSequence) - Remove
* (0008, 1140) (ReferencedImageSequence) - Remove
* (0008, 1155) (ReferencedSOPInstanceUID) - HashUID
* (0008, 1195) (TransactionUID) - HashUID
* (0008, 2111) (DerivationDescription) - Clean
* (0008, 2112) (SourceImageSequence) - Remove
* (0008, 3010) (IrradiationEventUID) - HashUID
* (0008, 4000) (IdentifyingComments) - Clean
* (0010, 0010) (PatientName) - Empty
* (0010, 0020) (PatientID) - Empty
* (0010, 0021) (IssuerOfPatientID) - Remove
* (0010, 0030) (PatientBirthDate) - Empty
* (0010, 0032) (PatientBirthTime) - Remove
* (0010, 0040) (PatientSex) - Keep
* (0010, 0050) (PatientInsurancePlanCodeSequence) - Remove
* (0010, 0101) (PatientPrimaryLanguageCodeSequence) - Remove
* (0010, 0102) (PatientPrimaryLanguageModifierCodeSequence) - Remove
* (0010, 1000) (OtherPatientIDs) - Remove
* (0010, 1001) (OtherPatientNames) - Remove
* (0010, 1002) (OtherPatientIDsSequence) - Remove
* (0010, 1005) (PatientBirthName) - Remove
* (0010, 1010) (PatientAge) - Keep
* (0010, 1020) (PatientSize) - Keep
* (0010, 1030) (PatientWeight) - Keep
* (0010, 1040) (PatientAddress) - Remove
* (0010, 1050) (InsurancePlanIdentification) - Remove
* (0010, 1060) (PatientMotherBirthName) - Remove
* (0010, 1080) (MilitaryRank) - Remove
* (0010, 1081) (BranchOfService) - Remove
* (0010, 1090) (MedicalRecordLocator) - Remove
* (0010, 1100) (ReferencedPatientPhotoSequence) - Remove
* (0010, 2000) (MedicalAlerts) - Clean
* (0010, 2110) (Allergies) - Clean
* (0010, 2150) (CountryOfResidence) - Remove
* (0010, 2152) (RegionOfResidence) - Remove
* (0010, 2154) (PatientTelephoneNumbers) - Remove
* (0010, 2155) (PatientTelecomInformation) - Remove
* (0010, 2160) (EthnicGroup) - Keep
* (0010, 2180) (Occupation) - Clean
* (0010, 21a0) (SmokingStatus) - Keep
* (0010, 21b0) (AdditionalPatientHistory) - Clean
* (0010, 21c0) (PregnancyStatus) - Keep
* (0010, 21d0) (LastMenstrualDate) - Remove
* (0010, 21f0) (PatientReligiousPreference) - Remove
* (0010, 2203) (PatientSexNeutered) - Keep
* (0010, 2297) (ResponsiblePerson) - Remove
* (0010, 2299) (ResponsibleOrganization) - Remove
* (0010, 4000) (PatientComments) - Clean
* (0012, 0010) (ClinicalTrialSponsorName) - Replace
* (0012, 0020) (ClinicalTrialProtocolID) - Replace
* (0012, 0021) (ClinicalTrialProtocolName) - Empty
* (0012, 0030) (ClinicalTrialSiteID) - Empty
* (0012, 0031) (ClinicalTrialSiteName) - Empty
* (0012, 0040) (ClinicalTrialSubjectID) - Replace
* (0012, 0042) (ClinicalTrialSubjectReadingID) - Replace
* (0012, 0050) (ClinicalTrialTimePointID) - Empty
* (0012, 0051) (ClinicalTrialTimePointDescription) - Clean
* (0012, 0060) (ClinicalTrialCoordinatingCenterName) - Empty
* (0012, 0071) (ClinicalTrialSeriesID) - Remove
* (0012, 0072) (ClinicalTrialSeriesDescription) - Clean
* (0012, 0081) (ClinicalTrialProtocolEthicsCommitteeName) - Replace
* (0012, 0082) (ClinicalTrialProtocolEthicsCommitteeApprovalNumber) - Remove
* (0016, 002b) (MakerNote) - Clean
* (0016, 004b) (DeviceSettingDescription) - Clean
* (0016, 004d) (CameraOwnerName) - Remove
* (0016, 004e) (LensSpecification) - Keep
* (0016, 004f) (LensMake) - Keep
* (0016, 0050) (LensModel) - Keep
* (0016, 0051) (LensSerialNumber) - Keep
* (0016, 0070) (GPSVersionID) - Remove
* (0016, 0071) (GPSLatitudeRef) - Remove
* (0016, 0072) (GPSLatitude) - Remove
* (0016, 0073) (GPSLongitudeRef) - Remove
* (0016, 0074) (GPSLongitude) - Remove
* (0016, 0075) (GPSAltitudeRef) - Remove
* (0016, 0076) (GPSAltitude) - Remove
* (0016, 0077) (GPSTimeStamp) - Remove
* (0016, 0078) (GPSSatellites) - Remove
* (0016, 0079) (GPSStatus) - Remove
* (0016, 007a) (GPSMeasureMode) - Remove
* (0016, 007b) (GPSDOP) - Remove
* (0016, 007c) (GPSSpeedRef) - Remove
* (0016, 007d) (GPSSpeed) - Remove
* (0016, 007e) (GPSTrackRef) - Remove
* (0016, 007f) (GPSTrack) - Remove
* (0016, 0080) (GPSImgDirectionRef) - Remove
* (0016, 0081) (GPSImgDirection) - Remove
* (0016, 0082) (GPSMapDatum) - Remove
* (0016, 0083) (GPSDestLatitudeRef) - Remove
* (0016, 0084) (GPSDestLatitude) - Remove
* (0016, 0085) (GPSDestLongitudeRef) - Remove
* (0016, 0086) (GPSDestLongitude) - Remove
* (0016, 0087) (GPSDestBearingRef) - Remove
* (0016, 0088) (GPSDestBearing) - Remove
* (0016, 0089) (GPSDestDistanceRef) - Remove
* (0016, 008a) (GPSDestDistance) - Remove
* (0016, 008b) (GPSProcessingMethod) - Remove
* (0016, 008c) (GPSAreaInformation) - Remove
* (0016, 008d) (GPSDateStamp) - Remove
* (0016, 008e) (GPSDifferential) - Remove
* (0018, 0010) (ContrastBolusAgent) - Clean
* (0018, 1000) (DeviceSerialNumber) - Keep
* (0018, 1002) (DeviceUID) - Keep
* (0018, 1004) (PlateID) - Keep
* (0018, 1005) (GeneratorID) - Keep
* (0018, 1007) (CassetteID) - Keep
* (0018, 1008) (GantryID) - Keep
* (0018, 1009) (UniqueDeviceIdentifier) - Keep
* (0018, 100a) (UDISequence) - Keep
* (0018, 100b) (ManufacturerDeviceClassUID) - Keep
* (0018, 1030) (ProtocolName) - Clean
* (0018, 1400) (AcquisitionDeviceProcessingDescription) - Clean
* (0018, 2042) (TargetUID) - HashUID
* (0018, 4000) (AcquisitionComments) - Clean
* (0018, 700a) (DetectorID) - Keep
* (0018, 9185) (RespiratoryMotionCompensationTechniqueDescription) - Clean
* (0018, 9367) (XRaySourceID) - Keep
* (0018, 9369) (SourceStartDateTime) - Replace
* (0018, 936a) (SourceEndDateTime) - Replace
* (0018, 9371) (XRayDetectorID) - Keep
* (0018, 9373) (XRayDetectorLabel) - Keep
* (0018, 937b) (MultienergyAcquisitionDescription) - Clean
* (0018, 937f) (DecompositionDescription) - Clean
* (0018, 9424) (AcquisitionProtocolDescription) - Clean
* (0018, 9516) (StartAcquisitionDateTime) - Remove
* (0018, 9517) (EndAcquisitionDateTime) - Remove
* (0018, a003) (ContributionDescription) - Clean
* (0020, 000d) (StudyInstanceUID) - HashUID
* (0020, 000e) (SeriesInstanceUID) - HashUID
* (0020, 0010) (StudyID) - Empty
* (0020, 0052) (FrameOfReferenceUID) - HashUID
* (0020, 0200) (SynchronizationFrameOfReferenceUID) - HashUID
* (0020, 3401) (ModifyingDeviceID) - Remove
* (0020, 3406) (ModifiedImageDescription) - Remove
* (0020, 4000) (ImageComments) - Clean
* (0020, 9158) (FrameComments) - Clean
* (0020, 9161) (ConcatenationUID) - HashUID
* (0020, 9164) (DimensionOrganizationUID) - HashUID
* (0028, 1199) (PaletteColorLookupTableUID) - HashUID
* (0028, 1214) (LargePaletteColorLookupTableUID) - HashUID
* (0028, 4000) (ImagePresentationComments) - Remove
* (0032, 0012) (StudyIDIssuer) - Remove
* (0032, 1020) (ScheduledStudyLocation) - Keep
* (0032, 1021) (ScheduledStudyLocationAETitle) - Keep
* (0032, 1030) (ReasonForStudy) - Clean
* (0032, 1032) (RequestingPhysician) - Remove
* (0032, 1033) (RequestingService) - Remove
* (0032, 1060) (RequestedProcedureDescription) - Clean
* (0032, 1066) (ReasonForVisit) - Clean
* (0032, 1067) (ReasonForVisitCodeSequence) - Clean
* (0032, 1070) (RequestedContrastAgent) - Clean
* (0032, 4000) (StudyComments) - Clean
* (0034, 0001) (FlowIdentifierSequence) - Replace
* (0034, 0002) (FlowIdentifier) - Replace
* (0034, 0005) (SourceIdentifier) - Replace
* (0034, 0007) (FrameOriginTimestamp) - Replace
* (0038, 0004) (ReferencedPatientAliasSequence) - Remove
* (0038, 0010) (AdmissionID) - Remove
* (0038, 0011) (IssuerOfAdmissionID) - Remove
* (0038, 0014) (IssuerOfAdmissionIDSequence) - Remove
* (0038, 001e) (ScheduledPatientInstitutionResidence) - Remove
* (0038, 0020) (AdmittingDate) - Remove
* (0038, 0021) (AdmittingTime) - Remove
* (0038, 0040) (DischargeDiagnosisDescription) - Clean
* (0038, 0050) (SpecialNeeds) - Clean
* (0038, 0060) (ServiceEpisodeID) - Remove
* (0038, 0061) (IssuerOfServiceEpisodeID) - Remove
* (0038, 0062) (ServiceEpisodeDescription) - Clean
* (0038, 0064) (IssuerOfServiceEpisodeIDSequence) - Remove
* (0038, 0300) (CurrentPatientLocation) - Remove
* (0038, 0400) (PatientInstitutionResidence) - Remove
* (0038, 0500) (PatientState) - Clean
* (0038, 4000) (VisitComments) - Clean
* (003a, 0310) (Unknown Tag) - HashUID
* (003a, 0314) (Unknown Tag) - Replace
* (0040, 0001) (ScheduledStationAETitle) - Keep
* (0040, 0002) (ScheduledProcedureStepStartDate) - Remove
* (0040, 0003) (ScheduledProcedureStepStartTime) - Remove
* (0040, 0004) (ScheduledProcedureStepEndDate) - Remove
* (0040, 0005) (ScheduledProcedureStepEndTime) - Remove
* (0040, 0006) (ScheduledPerformingPhysicianName) - Remove
* (0040, 0007) (ScheduledProcedureStepDescription) - Clean
* (0040, 000b) (ScheduledPerformingPhysicianIdentificationSequence) - Remove
* (0040, 0010) (ScheduledStationName) - Keep
* (0040, 0011) (ScheduledProcedureStepLocation) - Keep
* (0040, 0012) (PreMedication) - Clean
* (0040, 0241) (PerformedStationAETitle) - Keep
* (0040, 0242) (PerformedStationName) - Keep
* (0040, 0243) (PerformedLocation) - Remove
* (0040, 0244) (PerformedProcedureStepStartDate) - Remove
* (0040, 0245) (PerformedProcedureStepStartTime) - Remove
* (0040, 0250) (PerformedProcedureStepEndDate) - Remove
* (0040, 0251) (PerformedProcedureStepEndTime) - Remove
* (0040, 0253) (PerformedProcedureStepID) - Remove
* (0040, 0254) (PerformedProcedureStepDescription) - Clean
* (0040, 0275) (RequestAttributesSequence) - Clean
* (0040, 0280) (CommentsOnThePerformedProcedureStep) - Clean
* (0040, 050a) (SpecimenAccessionNumber) - Remove
* (0040, 0512) (ContainerIdentifier) - Replace
* (0040, 0513) (IssuerOfTheContainerIdentifierSequence) - Empty
* (0040, 051a) (ContainerDescription) - Clean
* (0040, 0551) (SpecimenIdentifier) - Replace
* (0040, 0554) (SpecimenUID) - HashUID
* (0040, 0555) (AcquisitionContextSequence) - Remove
* (0040, 0562) (IssuerOfTheSpecimenIdentifierSequence) - Empty
* (0040, 0600) (SpecimenShortDescription) - Clean
* (0040, 0602) (SpecimenDetailedDescription) - Clean
* (0040, 0610) (SpecimenPreparationSequence) - Empty
* (0040, 06fa) (SlideIdentifier) - Remove
* (0040, 1001) (RequestedProcedureID) - Remove
* (0040, 1002) (ReasonForTheRequestedProcedure) - Clean
* (0040, 1004) (PatientTransportArrangements) - Remove
* (0040, 1005) (RequestedProcedureLocation) - Remove
* (0040, 100a) (ReasonForRequestedProcedureCodeSequence) - Clean
* (0040, 1010) (NamesOfIntendedRecipientsOfResults) - Remove
* (0040, 1011) (IntendedRecipientsOfResultsIdentificationSequence) - Remove
* (0040, 1101) (PersonIdentificationCodeSequence) - Replace
* (0040, 1102) (PersonAddress) - Remove
* (0040, 1103) (PersonTelephoneNumbers) - Remove
* (0040, 1104) (PersonTelecomInformation) - Remove
* (0040, 1400) (RequestedProcedureComments) - Clean
* (0040, 2001) (ReasonForTheImagingServiceRequest) - Clean
* (0040, 2008) (OrderEnteredBy) - Remove
* (0040, 2009) (OrderEntererLocation) - Remove
* (0040, 2010) (OrderCallbackPhoneNumber) - Remove
* (0040, 2011) (OrderCallbackTelecomInformation) - Remove
* (0040, 2016) (PlacerOrderNumberImagingServiceRequest) - Empty
* (0040, 2017) (FillerOrderNumberImagingServiceRequest) - Empty
* (0040, 2400) (ImagingServiceRequestComments) - Clean
* (0040, 3001) (ConfidentialityConstraintOnPatientDataDescription) - Remove
* (0040, 4005) (ScheduledProcedureStepStartDateTime) - Remove
* (0040, 4008) (ScheduledProcedureStepExpirationDateTime) - Remove
* (0040, 4010) (ScheduledProcedureStepModificationDateTime) - Remove
* (0040, 4011) (ExpectedCompletionDateTime) - Remove
* (0040, 4023) (ReferencedGeneralPurposeScheduledProcedureStepTransactionUID) - HashUID
* (0040, 4025) (ScheduledStationNameCodeSequence) - Keep
* (0040, 4027) (ScheduledStationGeographicLocationCodeSequence) - Keep
* (0040, 4028) (PerformedStationNameCodeSequence) - Keep
* (0040, 4030) (PerformedStationGeographicLocationCodeSequence) - Keep
* (0040, 4034) (ScheduledHumanPerformersSequence) - Remove
* (0040, 4035) (ActualHumanPerformersSequence) - Remove
* (0040, 4036) (HumanPerformerOrganization) - Remove
* (0040, 4037) (HumanPerformerName) - Remove
* (0040, 4050) (PerformedProcedureStepStartDateTime) - Remove
* (0040, 4051) (PerformedProcedureStepEndDateTime) - Remove
* (0040, 4052) (ProcedureStepCancellationDateTime) - Remove
* (0040, a027) (VerifyingOrganization) - Replace
* (0040, a073) (VerifyingObserverSequence) - Replace
* (0040, a075) (VerifyingObserverName) - Replace
* (0040, a078) (AuthorObserverSequence) - Remove
* (0040, a07a) (ParticipantSequence) - Remove
* (0040, a07c) (CustodialOrganizationSequence) - Remove
* (0040, a088) (VerifyingObserverIdentificationCodeSequence) - Empty
* (0040, a123) (PersonName) - Replace
* (0040, a124) (UID) - HashUID
* (0040, a171) (ObservationUID) - HashUID
* (0040, a172) (ReferencedObservationUIDTrial) - HashUID
* (0040, a192) (ObservationDateTrial) - Remove
* (0040, a193) (ObservationTimeTrial) - Remove
* (0040, a307) (CurrentObserverTrial) - Remove
* (0040, a352) (VerbalSourceTrial) - Remove
* (0040, a353) (AddressTrial) - Remove
* (0040, a354) (TelephoneNumberTrial) - Remove
* (0040, a358) (VerbalSourceIdentifierCodeSequenceTrial) - Remove
* (0040, a402) (ObservationSubjectUIDTrial) - HashUID
* (0040, a730) (ContentSequence) - Replace
* (0040, db0c) (TemplateExtensionOrganizationUID) - HashUID
* (0040, db0d) (TemplateExtensionCreatorUID) - HashUID
* (0050, 001b) (ContainerComponentID) - Remove
* (0050, 0020) (DeviceDescription) - Keep
* (0050, 0021) (LongDeviceDescription) - Clean
* (0062, 0021) (TrackingUID) - HashUID
* (0070, 0001) (GraphicAnnotationSequence) - Replace
* (0070, 0084) (ContentCreatorName) - Replace
* (0070, 0086) (ContentCreatorIdentificationCodeSequence) - Remove
* (0070, 031a) (FiducialUID) - HashUID
* (0070, 1101) (PresentationDisplayCollectionUID) - HashUID
* (0070, 1102) (PresentationSequenceCollectionUID) - HashUID
* (0088, 0140) (StorageMediaFileSetUID) - HashUID
* (0088, 0200) (IconImageSequence) - Remove
* (0088, 0904) (TopicTitle) - Remove
* (0088, 0906) (TopicSubject) - Remove
* (0088, 0910) (TopicAuthor) - Remove
* (0088, 0912) (TopicKeywords) - Remove
* (0400, 0100) (DigitalSignatureUID) - HashUID
* (0400, 0402) (ReferencedDigitalSignatureSequence) - Remove
* (0400, 0403) (ReferencedSOPInstanceMACSequence) - Remove
* (0400, 0404) (MAC) - Remove
* (0400, 0550) (ModifiedAttributesSequence) - Remove
* (0400, 0561) (OriginalAttributesSequence) - Remove
* (0400, 0600) (InstanceOriginStatus) - Remove
* (2030, 0020) (TextString) - Remove
* (2200, 0002) (LabelText) - Clean
* (2200, 0005) (BarcodeValue) - Remove
* (3006, 0024) (ReferencedFrameOfReferenceUID) - HashUID
* (3006, 00c2) (RelatedFrameOfReferenceUID) - HashUID
* (3008, 0054) (FirstTreatmentDate) - Remove
* (3008, 0056) (MostRecentTreatmentDate) - Remove
* (3008, 0105) (SourceSerialNumber) - Keep
* (3008, 0250) (TreatmentDate) - Remove
* (3008, 0251) (TreatmentTime) - Remove
* (300a, 0002) (RTPlanLabel) - Clean
* (300a, 0003) (RTPlanName) - Clean
* (300a, 0004) (RTPlanDescription) - Clean
* (300a, 0006) (RTPlanDate) - Remove
* (300a, 0007) (RTPlanTime) - Remove
* (300a, 000e) (PrescriptionDescription) - Clean
* (300a, 0013) (DoseReferenceUID) - HashUID
* (300a, 0016) (DoseReferenceDescription) - Clean
* (300a, 0072) (FractionGroupDescription) - Clean
* (300a, 0083) (ReferencedDoseReferenceUID) - HashUID
* (300a, 00b2) (TreatmentMachineName) - Keep
* (300a, 00c3) (BeamDescription) - Clean
* (300a, 00dd) (BolusDescription) - Clean
* (300a, 0196) (FixationDeviceDescription) - Clean
* (300a, 01a6) (ShieldingDeviceDescription) - Clean
* (300a, 01b2) (SetupTechniqueDescription) - Clean
* (300a, 0216) (SourceManufacturer) - Keep
* (300a, 02eb) (CompensatorDescription) - Clean
* (300a, 0608) (TreatmentPositionGroupLabel) - Clean
* (300a, 0609) (TreatmentPositionGroupUID) - HashUID
* (300a, 0611) (RTAccessoryHolderSlotID) - Empty
* (300a, 0615) (RTAccessoryDeviceSlotID) - Empty
* (300a, 0619) (RadiationDoseIdentificationLabel) - Clean
* (300a, 0623) (RadiationDoseInVivoMeasurementLabel) - Clean
* (300a, 062a) (RTToleranceSetLabel) - Clean
* (300a, 0650) (PatientSetupUID) - HashUID
* (300a, 0676) (EquipmentFrameOfReferenceDescription) - Clean
* (300a, 067c) (RadiationGenerationModeLabel) - Clean
* (300a, 067d) (RadiationGenerationModeDescription) - Clean
* (300a, 0700) (Unknown Tag) - HashUID
* (300a, 0734) (Unknown Tag) - Clean
* (300a, 0736) (Unknown Tag) - Replace
* (300a, 073a) (Unknown Tag) - Replace
* (300a, 0741) (Unknown Tag) - Replace
* (300a, 0742) (Unknown Tag) - Clean
* (300a, 0760) (Unknown Tag) - Replace
* (300a, 0783) (Unknown Tag) - Clean
* (300c, 0113) (ReasonForOmissionDescription) - Clean
* (300e, 0008) (ReviewerName) - Remove
* (3010, 0006) (ConceptualVolumeUID) - HashUID
* (3010, 000b) (ReferencedConceptualVolumeUID) - HashUID
* (3010, 000f) (ConceptualVolumeCombinationDescription) - Clean
* (3010, 0013) (ConstituentConceptualVolumeUID) - HashUID
* (3010, 0015) (SourceConceptualVolumeUID) - HashUID
* (3010, 0017) (ConceptualVolumeDescription) - Clean
* (3010, 001b) (DeviceAlternateIdentifier) - Empty
* (3010, 002d) (DeviceLabel) - Keep
* (3010, 0031) (ReferencedFiducialsUID) - HashUID
* (3010, 0033) (UserContentLabel) - Clean
* (3010, 0034) (UserContentLongLabel) - Clean
* (3010, 0035) (EntityLabel) - Clean
* (3010, 0036) (EntityName) - Clean
* (3010, 0037) (EntityDescription) - Clean
* (3010, 0038) (EntityLongLabel) - Clean
* (3010, 003b) (RTTreatmentPhaseUID) - HashUID
* (3010, 0043) (ManufacturerDeviceIdentifier) - Keep
* (3010, 004c) (IntendedPhaseStartDate) - Remove
* (3010, 004d) (IntendedPhaseEndDate) - Remove
* (3010, 0054) (RTPrescriptionLabel) - Clean
* (3010, 0056) (RTTreatmentApproachLabel) - Clean
* (3010, 005a) (RTPhysicianIntentNarrative) - Clean
* (3010, 005c) (ReasonForSuperseding) - Clean
* (3010, 0061) (PriorTreatmentDoseDescription) - Clean
* (3010, 006e) (DosimetricObjectiveUID) - HashUID
* (3010, 006f) (ReferencedDosimetricObjectiveUID) - HashUID
* (3010, 0077) (TreatmentSite) - Clean
* (3010, 007a) (TreatmentTechniqueNotes) - Clean
* (3010, 007b) (PrescriptionNotes) - Clean
* (3010, 007f) (FractionationNotes) - Clean
* (3010, 0081) (PrescriptionNotesSequence) - Clean
* (4000, 0010) (Arbitrary) - Remove
* (4000, 4000) (TextComments) - Remove
* (4008, 0042) (ResultsIDIssuer) - Remove
* (4008, 0102) (InterpretationRecorder) - Remove
* (4008, 010a) (InterpretationTranscriber) - Remove
* (4008, 010b) (InterpretationText) - Clean
* (4008, 010c) (InterpretationAuthor) - Remove
* (4008, 0111) (InterpretationApproverSequence) - Remove
* (4008, 0114) (PhysicianApprovingInterpretation) - Remove
* (4008, 0115) (InterpretationDiagnosisDescription) - Clean
* (4008, 0118) (ResultsDistributionListSequence) - Remove
* (4008, 0119) (DistributionName) - Remove
* (4008, 011a) (DistributionAddress) - Remove
* (4008, 0202) (InterpretationIDIssuer) - Remove
* (4008, 0300) (Impressions) - Clean
* (4008, 4000) (ResultsComments) - Clean
* (50xx, xxxx) (Unknown Repeater tag 50xxxxxx) - Remove
* (60xx, 3000) (OverlayData) - Remove
* (60xx, 4000) (OverlayComments) - Remove
* (fffa, fffa) (DigitalSignaturesSequence) - Remove
* (fffc, fffc) (DataSetTrailingPadding) - Remove
* PrivateAttributes (Private Attributes) - Clean
