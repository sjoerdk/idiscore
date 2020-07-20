"""Public DICOM information auto-generated from generate_public_dicom.py

Information from table E.1-1 here:
http://dicom.nema.org/medical/dicom/current/output/chtml/part15/chapter_E.html
"""

from idiscore.nema import ActionCodes, RawNemaRuleSet
from idiscore.identifiers import SingleTag, RepeatingGroup, PrivateTags

basic_profile = RawNemaRuleSet(
    name="Basic Application Level Confidentiality Profile",
    code="113100",
    rules=[
        (SingleTag("00080050"), ActionCodes.EMPTY),  # AccessionNumber
        (SingleTag("00184000"), ActionCodes.REMOVE),  # AcquisitionComments
        (
            SingleTag("00400555"),
            ActionCodes.REMOVE_OR_EMPTY,
        ),  # AcquisitionContextSequence
        (SingleTag("00080022"), ActionCodes.REMOVE_OR_EMPTY),  # AcquisitionDate
        (
            SingleTag("0008002a"),
            ActionCodes.REMOVE_OR_EMPTY_OR_DUMMY,
        ),  # AcquisitionDateTime
        (
            SingleTag("00181400"),
            ActionCodes.REMOVE_OR_DUMMY,
        ),  # AcquisitionDeviceProcessingDescription
        (SingleTag("00189424"), ActionCodes.REMOVE),  # AcquisitionProtocolDescription
        (SingleTag("00080032"), ActionCodes.REMOVE_OR_EMPTY),  # AcquisitionTime
        (SingleTag("00404035"), ActionCodes.REMOVE),  # ActualHumanPerformersSequence
        (SingleTag("001021b0"), ActionCodes.REMOVE),  # AdditionalPatientHistory
        (SingleTag("0040a353"), ActionCodes.REMOVE),  # AddressTrial
        (SingleTag("00380010"), ActionCodes.REMOVE),  # AdmissionID
        (SingleTag("00380020"), ActionCodes.REMOVE),  # AdmittingDate
        (SingleTag("00081084"), ActionCodes.REMOVE),  # AdmittingDiagnosesCodeSequence
        (SingleTag("00081080"), ActionCodes.REMOVE),  # AdmittingDiagnosesDescription
        (SingleTag("00380021"), ActionCodes.REMOVE),  # AdmittingTime
        (SingleTag("00001000"), ActionCodes.REMOVE),  # AffectedSOPInstanceUID
        (SingleTag("00102110"), ActionCodes.REMOVE),  # Allergies
        (SingleTag("40000010"), ActionCodes.REMOVE),  # Arbitrary
        (SingleTag("0040a078"), ActionCodes.REMOVE),  # AuthorObserverSequence
        (SingleTag("22000005"), ActionCodes.REMOVE_OR_EMPTY),  # BarcodeValue
        (SingleTag("300a00c3"), ActionCodes.REMOVE),  # BeamDescription
        (SingleTag("300a00dd"), ActionCodes.REMOVE),  # BolusDescription
        (SingleTag("00101081"), ActionCodes.REMOVE),  # BranchOfService
        (SingleTag("0016004d"), ActionCodes.REMOVE),  # CameraOwnerName
        (SingleTag("00181007"), ActionCodes.REMOVE),  # CassetteID
        (
            SingleTag("00120060"),
            ActionCodes.EMPTY,
        ),  # ClinicalTrialCoordinatingCenterName
        (
            SingleTag("00120082"),
            ActionCodes.REMOVE,
        ),  # ClinicalTrialProtocolEthicsCommitteeApprovalNumber
        (
            SingleTag("00120081"),
            ActionCodes.DUMMY,
        ),  # ClinicalTrialProtocolEthicsCommitteeName
        (SingleTag("00120020"), ActionCodes.DUMMY),  # ClinicalTrialProtocolID
        (SingleTag("00120021"), ActionCodes.EMPTY),  # ClinicalTrialProtocolName
        (SingleTag("00120072"), ActionCodes.REMOVE),  # ClinicalTrialSeriesDescription
        (SingleTag("00120071"), ActionCodes.REMOVE),  # ClinicalTrialSeriesID
        (SingleTag("00120030"), ActionCodes.EMPTY),  # ClinicalTrialSiteID
        (SingleTag("00120031"), ActionCodes.EMPTY),  # ClinicalTrialSiteName
        (SingleTag("00120010"), ActionCodes.DUMMY),  # ClinicalTrialSponsorName
        (SingleTag("00120040"), ActionCodes.DUMMY),  # ClinicalTrialSubjectID
        (SingleTag("00120042"), ActionCodes.DUMMY),  # ClinicalTrialSubjectReadingID
        (
            SingleTag("00120051"),
            ActionCodes.REMOVE,
        ),  # ClinicalTrialTimePointDescription
        (SingleTag("00120050"), ActionCodes.EMPTY),  # ClinicalTrialTimePointID
        (
            SingleTag("00400280"),
            ActionCodes.REMOVE,
        ),  # CommentsOnThePerformedProcedureStep
        (SingleTag("300a02eb"), ActionCodes.REMOVE),  # CompensatorDescription
        (SingleTag("00209161"), ActionCodes.UID),  # ConcatenationUID
        (
            SingleTag("3010000f"),
            ActionCodes.EMPTY,
        ),  # ConceptualVolumeCombinationDescription
        (SingleTag("30100017"), ActionCodes.EMPTY),  # ConceptualVolumeDescription
        (SingleTag("30100006"), ActionCodes.UID),  # ConceptualVolumeUID
        (
            SingleTag("00403001"),
            ActionCodes.REMOVE,
        ),  # ConfidentialityConstraintOnPatientDataDescription
        (SingleTag("30100013"), ActionCodes.UID),  # ConstituentConceptualVolumeUID
        (SingleTag("0008009c"), ActionCodes.EMPTY),  # ConsultingPhysicianName
        (
            SingleTag("0008009d"),
            ActionCodes.REMOVE,
        ),  # ConsultingPhysicianIdentificationSequence
        (SingleTag("0050001b"), ActionCodes.REMOVE),  # ContainerComponentID
        (SingleTag("0040051a"), ActionCodes.REMOVE),  # ContainerDescription
        (SingleTag("00400512"), ActionCodes.DUMMY),  # ContainerIdentifier
        (
            SingleTag("00700086"),
            ActionCodes.REMOVE,
        ),  # ContentCreatorIdentificationCodeSequence
        (SingleTag("00700084"), ActionCodes.REPLACE_OR_DUMMY),  # ContentCreatorName
        (SingleTag("00080023"), ActionCodes.REPLACE_OR_DUMMY),  # ContentDate
        (SingleTag("0040a730"), ActionCodes.DUMMY),  # ContentSequence
        (SingleTag("00080033"), ActionCodes.REPLACE_OR_DUMMY),  # ContentTime
        (SingleTag("00180010"), ActionCodes.REPLACE_OR_DUMMY),  # ContrastBolusAgent
        (SingleTag("0018a003"), ActionCodes.REMOVE),  # ContributionDescription
        (SingleTag("00102150"), ActionCodes.REMOVE),  # CountryOfResidence
        (SingleTag("0040a307"), ActionCodes.REMOVE),  # CurrentObserverTrial
        (SingleTag("00380300"), ActionCodes.REMOVE),  # CurrentPatientLocation
        (
            RepeatingGroup("50xxxxxx"),
            ActionCodes.REMOVE,
        ),  # Unknown Repeater tag 50xxxxxx
        (SingleTag("00080025"), ActionCodes.REMOVE),  # CurveDate
        (SingleTag("00080035"), ActionCodes.REMOVE),  # CurveTime
        (SingleTag("0040a07c"), ActionCodes.REMOVE),  # CustodialOrganizationSequence
        (SingleTag("fffcfffc"), ActionCodes.REMOVE),  # DataSetTrailingPadding
        (SingleTag("0018937f"), ActionCodes.REMOVE),  # DecompositionDescription
        (SingleTag("00082111"), ActionCodes.REMOVE),  # DerivationDescription
        (SingleTag("0018700a"), ActionCodes.REMOVE_OR_DUMMY),  # DetectorID
        (SingleTag("3010001b"), ActionCodes.EMPTY),  # DeviceAlternateIdentifier
        (SingleTag("00500020"), ActionCodes.REMOVE),  # DeviceDescription
        (SingleTag("3010002d"), ActionCodes.DUMMY),  # DeviceLabel
        (
            SingleTag("00181000"),
            ActionCodes.REMOVE_OR_EMPTY_OR_DUMMY,
        ),  # DeviceSerialNumber
        (SingleTag("0016004b"), ActionCodes.REMOVE),  # DeviceSettingDescription
        (SingleTag("00181002"), ActionCodes.UID),  # DeviceUID
        (SingleTag("fffafffa"), ActionCodes.REMOVE),  # DigitalSignaturesSequence
        (SingleTag("04000100"), ActionCodes.UID),  # DigitalSignatureUID
        (SingleTag("00209164"), ActionCodes.UID),  # DimensionOrganizationUID
        (SingleTag("00380040"), ActionCodes.REMOVE),  # DischargeDiagnosisDescription
        (SingleTag("4008011a"), ActionCodes.REMOVE),  # DistributionAddress
        (SingleTag("40080119"), ActionCodes.REMOVE),  # DistributionName
        (SingleTag("300a0016"), ActionCodes.REMOVE),  # DoseReferenceDescription
        (SingleTag("300a0013"), ActionCodes.UID),  # DoseReferenceUID
        (SingleTag("3010006e"), ActionCodes.UID),  # DosimetricObjectiveUID
        (SingleTag("00189517"), ActionCodes.REMOVE_OR_DUMMY),  # EndAcquisitionDateTime
        (SingleTag("30100037"), ActionCodes.REMOVE),  # EntityDescription
        (SingleTag("30100035"), ActionCodes.DUMMY),  # EntityLabel
        (SingleTag("30100038"), ActionCodes.DUMMY),  # EntityLongLabel
        (SingleTag("30100036"), ActionCodes.REMOVE),  # EntityName
        (
            SingleTag("300a0676"),
            ActionCodes.REMOVE,
        ),  # EquipmentFrameOfReferenceDescription
        (SingleTag("00102160"), ActionCodes.REMOVE),  # EthnicGroup
        (SingleTag("00404011"), ActionCodes.REMOVE),  # ExpectedCompletionDateTime
        (SingleTag("00080058"), ActionCodes.UID),  # FailedSOPInstanceUIDList
        (SingleTag("0070031a"), ActionCodes.UID),  # FiducialUID
        (
            SingleTag("00402017"),
            ActionCodes.EMPTY,
        ),  # FillerOrderNumberImagingServiceRequest
        (SingleTag("30080054"), ActionCodes.REMOVE_OR_DUMMY),  # FirstTreatmentDate
        (SingleTag("300a0196"), ActionCodes.REMOVE),  # FixationDeviceDescription
        (SingleTag("00340002"), ActionCodes.DUMMY),  # FlowIdentifier
        (SingleTag("00340001"), ActionCodes.DUMMY),  # FlowIdentifierSequence
        (SingleTag("3010007f"), ActionCodes.EMPTY),  # FractionationNotes
        (SingleTag("300a0072"), ActionCodes.REMOVE),  # FractionGroupDescription
        (SingleTag("00209158"), ActionCodes.REMOVE),  # FrameComments
        (SingleTag("00200052"), ActionCodes.UID),  # FrameOfReferenceUID
        (SingleTag("00340007"), ActionCodes.DUMMY),  # FrameOriginTimestamp
        (SingleTag("00181008"), ActionCodes.REMOVE),  # GantryID
        (SingleTag("00181005"), ActionCodes.REMOVE),  # GeneratorID
        (SingleTag("00160076"), ActionCodes.REMOVE),  # GPSAltitude
        (SingleTag("00160075"), ActionCodes.REMOVE),  # GPSAltitudeRef
        (SingleTag("0016008c"), ActionCodes.REMOVE),  # GPSAreaInformation
        (SingleTag("0016008d"), ActionCodes.REMOVE),  # GPSDateStamp
        (SingleTag("00160088"), ActionCodes.REMOVE),  # GPSDestBearing
        (SingleTag("00160087"), ActionCodes.REMOVE),  # GPSDestBearingRef
        (SingleTag("0016008a"), ActionCodes.REMOVE),  # GPSDestDistance
        (SingleTag("00160089"), ActionCodes.REMOVE),  # GPSDestDistanceRef
        (SingleTag("00160084"), ActionCodes.REMOVE),  # GPSDestLatitude
        (SingleTag("00160083"), ActionCodes.REMOVE),  # GPSDestLatitudeRef
        (SingleTag("00160086"), ActionCodes.REMOVE),  # GPSDestLongitude
        (SingleTag("00160085"), ActionCodes.REMOVE),  # GPSDestLongitudeRef
        (SingleTag("0016008e"), ActionCodes.REMOVE),  # GPSDifferential
        (SingleTag("0016007b"), ActionCodes.REMOVE),  # GPSDOP
        (SingleTag("00160081"), ActionCodes.REMOVE),  # GPSImgDirection
        (SingleTag("00160080"), ActionCodes.REMOVE),  # GPSImgDirectionRef
        (SingleTag("00160072"), ActionCodes.REMOVE),  # GPSLatitude
        (SingleTag("00160071"), ActionCodes.REMOVE),  # GPSLatitudeRef
        (SingleTag("00160074"), ActionCodes.REMOVE),  # GPSLongitude
        (SingleTag("00160073"), ActionCodes.REMOVE),  # GPSLongitudeRef
        (SingleTag("00160082"), ActionCodes.REMOVE),  # GPSMapDatum
        (SingleTag("0016007a"), ActionCodes.REMOVE),  # GPSMeasureMode
        (SingleTag("0016008b"), ActionCodes.REMOVE),  # GPSProcessingMethod
        (SingleTag("00160078"), ActionCodes.REMOVE),  # GPSSatellites
        (SingleTag("0016007d"), ActionCodes.REMOVE),  # GPSSpeed
        (SingleTag("0016007c"), ActionCodes.REMOVE),  # GPSSpeedRef
        (SingleTag("00160079"), ActionCodes.REMOVE),  # GPSStatus
        (SingleTag("00160077"), ActionCodes.REMOVE),  # GPSTimeStamp
        (SingleTag("0016007f"), ActionCodes.REMOVE),  # GPSTrack
        (SingleTag("0016007e"), ActionCodes.REMOVE),  # GPSTrackRef
        (SingleTag("00160070"), ActionCodes.REMOVE),  # GPSVersionID
        (SingleTag("00700001"), ActionCodes.DUMMY),  # GraphicAnnotationSequence
        (SingleTag("00404037"), ActionCodes.REMOVE),  # HumanPerformerName
        (SingleTag("00404036"), ActionCodes.REMOVE),  # HumanPerformerOrganization
        (SingleTag("00880200"), ActionCodes.REMOVE),  # IconImageSequence
        (SingleTag("00084000"), ActionCodes.REMOVE),  # IdentifyingComments
        (SingleTag("00204000"), ActionCodes.REMOVE),  # ImageComments
        (SingleTag("00284000"), ActionCodes.REMOVE),  # ImagePresentationComments
        (SingleTag("00402400"), ActionCodes.REMOVE),  # ImagingServiceRequestComments
        (SingleTag("003a0314"), ActionCodes.DUMMY),  # Unknown Tag
        (SingleTag("40080300"), ActionCodes.REMOVE),  # Impressions
        (SingleTag("00080015"), ActionCodes.REMOVE),  # InstanceCoercionDateTime
        (SingleTag("00080014"), ActionCodes.UID),  # InstanceCreatorUID
        (SingleTag("04000600"), ActionCodes.REMOVE),  # InstanceOriginStatus
        (SingleTag("00080081"), ActionCodes.REMOVE),  # InstitutionAddress
        (SingleTag("00081040"), ActionCodes.REMOVE),  # InstitutionalDepartmentName
        (
            SingleTag("00081041"),
            ActionCodes.REMOVE,
        ),  # InstitutionalDepartmentTypeCodeSequence
        (
            SingleTag("00080082"),
            ActionCodes.REMOVE_OR_EMPTY_OR_DUMMY,
        ),  # InstitutionCodeSequence
        (
            SingleTag("00080080"),
            ActionCodes.REMOVE_OR_EMPTY_OR_DUMMY,
        ),  # InstitutionName
        (SingleTag("00101050"), ActionCodes.REMOVE),  # InsurancePlanIdentification
        (SingleTag("3010004d"), ActionCodes.REMOVE_OR_DUMMY),  # IntendedPhaseEndDate
        (SingleTag("3010004c"), ActionCodes.REMOVE_OR_DUMMY),  # IntendedPhaseStartDate
        (
            SingleTag("00401011"),
            ActionCodes.REMOVE,
        ),  # IntendedRecipientsOfResultsIdentificationSequence
        (SingleTag("300a0741"), ActionCodes.DUMMY),  # Unknown Tag
        (SingleTag("300a0742"), ActionCodes.DUMMY),  # Unknown Tag
        (SingleTag("300a0783"), ActionCodes.DUMMY),  # Unknown Tag
        (SingleTag("40080111"), ActionCodes.REMOVE),  # InterpretationApproverSequence
        (SingleTag("4008010c"), ActionCodes.REMOVE),  # InterpretationAuthor
        (
            SingleTag("40080115"),
            ActionCodes.REMOVE,
        ),  # InterpretationDiagnosisDescription
        (SingleTag("40080202"), ActionCodes.REMOVE),  # InterpretationIDIssuer
        (SingleTag("40080102"), ActionCodes.REMOVE),  # InterpretationRecorder
        (SingleTag("4008010b"), ActionCodes.REMOVE),  # InterpretationText
        (SingleTag("4008010a"), ActionCodes.REMOVE),  # InterpretationTranscriber
        (SingleTag("00083010"), ActionCodes.UID),  # IrradiationEventUID
        (SingleTag("00380011"), ActionCodes.REMOVE),  # IssuerOfAdmissionID
        (SingleTag("00380014"), ActionCodes.REMOVE),  # IssuerOfAdmissionIDSequence
        (SingleTag("00100021"), ActionCodes.REMOVE),  # IssuerOfPatientID
        (SingleTag("00380061"), ActionCodes.REMOVE),  # IssuerOfServiceEpisodeID
        (SingleTag("00380064"), ActionCodes.REMOVE),  # IssuerOfServiceEpisodeIDSequence
        (
            SingleTag("00400513"),
            ActionCodes.EMPTY,
        ),  # IssuerOfTheContainerIdentifierSequence
        (
            SingleTag("00400562"),
            ActionCodes.EMPTY,
        ),  # IssuerOfTheSpecimenIdentifierSequence
        (SingleTag("22000002"), ActionCodes.REMOVE_OR_EMPTY),  # LabelText
        (SingleTag("00281214"), ActionCodes.UID),  # LargePaletteColorLookupTableUID
        (SingleTag("001021d0"), ActionCodes.REMOVE),  # LastMenstrualDate
        (SingleTag("0016004f"), ActionCodes.REMOVE),  # LensMake
        (SingleTag("00160050"), ActionCodes.REMOVE),  # LensModel
        (SingleTag("00160051"), ActionCodes.REMOVE),  # LensSerialNumber
        (SingleTag("0016004e"), ActionCodes.REMOVE),  # LensSpecification
        (SingleTag("00500021"), ActionCodes.REMOVE),  # LongDeviceDescription
        (SingleTag("04000404"), ActionCodes.REMOVE),  # MAC
        (SingleTag("0016002b"), ActionCodes.REMOVE),  # MakerNote
        (SingleTag("0018100b"), ActionCodes.UID),  # ManufacturerDeviceClassUID
        (SingleTag("30100043"), ActionCodes.EMPTY),  # ManufacturerDeviceIdentifier
        (SingleTag("00020003"), ActionCodes.UID),  # MediaStorageSOPInstanceUID
        (SingleTag("00102000"), ActionCodes.REMOVE),  # MedicalAlerts
        (SingleTag("00101090"), ActionCodes.REMOVE),  # MedicalRecordLocator
        (SingleTag("00101080"), ActionCodes.REMOVE),  # MilitaryRank
        (SingleTag("04000550"), ActionCodes.REMOVE),  # ModifiedAttributesSequence
        (SingleTag("00203406"), ActionCodes.REMOVE),  # ModifiedImageDescription
        (SingleTag("00203401"), ActionCodes.REMOVE),  # ModifyingDeviceID
        (SingleTag("30080056"), ActionCodes.REMOVE_OR_DUMMY),  # MostRecentTreatmentDate
        (
            SingleTag("0018937b"),
            ActionCodes.REMOVE,
        ),  # MultienergyAcquisitionDescription
        (SingleTag("003a0310"), ActionCodes.UID),  # Unknown Tag
        (SingleTag("00081060"), ActionCodes.REMOVE),  # NameOfPhysiciansReadingStudy
        (
            SingleTag("00401010"),
            ActionCodes.REMOVE,
        ),  # NamesOfIntendedRecipientsOfResults
        (SingleTag("0040a192"), ActionCodes.REMOVE),  # ObservationDateTrial
        (SingleTag("0040a402"), ActionCodes.UID),  # ObservationSubjectUIDTrial
        (SingleTag("0040a193"), ActionCodes.REMOVE),  # ObservationTimeTrial
        (SingleTag("0040a171"), ActionCodes.UID),  # ObservationUID
        (SingleTag("00102180"), ActionCodes.REMOVE),  # Occupation
        (
            SingleTag("00081072"),
            ActionCodes.REMOVE_OR_DUMMY,
        ),  # OperatorIdentificationSequence
        (SingleTag("00081070"), ActionCodes.REMOVE_OR_EMPTY_OR_DUMMY),  # OperatorsName
        (SingleTag("00402010"), ActionCodes.REMOVE),  # OrderCallbackPhoneNumber
        (SingleTag("00402011"), ActionCodes.REMOVE),  # OrderCallbackTelecomInformation
        (SingleTag("00402008"), ActionCodes.REMOVE),  # OrderEnteredBy
        (SingleTag("00402009"), ActionCodes.REMOVE),  # OrderEntererLocation
        (SingleTag("04000561"), ActionCodes.REMOVE),  # OriginalAttributesSequence
        (SingleTag("00101000"), ActionCodes.REMOVE),  # OtherPatientIDs
        (SingleTag("00101002"), ActionCodes.REMOVE),  # OtherPatientIDsSequence
        (SingleTag("00101001"), ActionCodes.REMOVE),  # OtherPatientNames
        (RepeatingGroup("60xx4000"), ActionCodes.REMOVE),  # OverlayComments
        (RepeatingGroup("60xx3000"), ActionCodes.REMOVE),  # OverlayData
        (SingleTag("00080024"), ActionCodes.REMOVE),  # OverlayDate
        (SingleTag("00080034"), ActionCodes.REMOVE),  # OverlayTime
        (SingleTag("300a0760"), ActionCodes.DUMMY),  # Unknown Tag
        (SingleTag("00281199"), ActionCodes.UID),  # PaletteColorLookupTableUID
        (SingleTag("0040a07a"), ActionCodes.REMOVE),  # ParticipantSequence
        (SingleTag("00101040"), ActionCodes.REMOVE),  # PatientAddress
        (SingleTag("00101010"), ActionCodes.REMOVE),  # PatientAge
        (SingleTag("00100030"), ActionCodes.EMPTY),  # PatientBirthDate
        (SingleTag("00101005"), ActionCodes.REMOVE),  # PatientBirthName
        (SingleTag("00100032"), ActionCodes.REMOVE),  # PatientBirthTime
        (SingleTag("00380400"), ActionCodes.REMOVE),  # PatientInstitutionResidence
        (SingleTag("00100050"), ActionCodes.REMOVE),  # PatientInsurancePlanCodeSequence
        (SingleTag("00101060"), ActionCodes.REMOVE),  # PatientMotherBirthName
        (SingleTag("00100010"), ActionCodes.EMPTY),  # PatientName
        (
            SingleTag("00100101"),
            ActionCodes.REMOVE,
        ),  # PatientPrimaryLanguageCodeSequence
        (
            SingleTag("00100102"),
            ActionCodes.REMOVE,
        ),  # PatientPrimaryLanguageModifierCodeSequence
        (SingleTag("001021f0"), ActionCodes.REMOVE),  # PatientReligiousPreference
        (SingleTag("00100040"), ActionCodes.EMPTY),  # PatientSex
        (SingleTag("00102203"), ActionCodes.REMOVE_OR_EMPTY),  # PatientSexNeutered
        (SingleTag("00101020"), ActionCodes.REMOVE),  # PatientSize
        (SingleTag("00102155"), ActionCodes.REMOVE),  # PatientTelecomInformation
        (SingleTag("00102154"), ActionCodes.REMOVE),  # PatientTelephoneNumbers
        (SingleTag("00101030"), ActionCodes.REMOVE),  # PatientWeight
        (SingleTag("00104000"), ActionCodes.REMOVE),  # PatientComments
        (SingleTag("00100020"), ActionCodes.EMPTY),  # PatientID
        (SingleTag("300a0650"), ActionCodes.UID),  # PatientSetupUID
        (SingleTag("00380500"), ActionCodes.REMOVE),  # PatientState
        (SingleTag("00401004"), ActionCodes.REMOVE),  # PatientTransportArrangements
        (SingleTag("00400243"), ActionCodes.REMOVE),  # PerformedLocation
        (
            SingleTag("00400254"),
            ActionCodes.REMOVE,
        ),  # PerformedProcedureStepDescription
        (SingleTag("00400250"), ActionCodes.REMOVE),  # PerformedProcedureStepEndDate
        (
            SingleTag("00404051"),
            ActionCodes.REMOVE,
        ),  # PerformedProcedureStepEndDateTime
        (SingleTag("00400251"), ActionCodes.REMOVE),  # PerformedProcedureStepEndTime
        (SingleTag("00400253"), ActionCodes.REMOVE),  # PerformedProcedureStepID
        (SingleTag("00400244"), ActionCodes.REMOVE),  # PerformedProcedureStepStartDate
        (
            SingleTag("00404050"),
            ActionCodes.REMOVE,
        ),  # PerformedProcedureStepStartDateTime
        (SingleTag("00400245"), ActionCodes.REMOVE),  # PerformedProcedureStepStartTime
        (SingleTag("00400241"), ActionCodes.REMOVE),  # PerformedStationAETitle
        (
            SingleTag("00404030"),
            ActionCodes.REMOVE,
        ),  # PerformedStationGeographicLocationCodeSequence
        (SingleTag("00400242"), ActionCodes.REMOVE),  # PerformedStationName
        (SingleTag("00404028"), ActionCodes.REMOVE),  # PerformedStationNameCodeSequence
        (SingleTag("00081050"), ActionCodes.REMOVE),  # PerformingPhysicianName
        (
            SingleTag("00081052"),
            ActionCodes.REMOVE,
        ),  # PerformingPhysicianIdentificationSequence
        (SingleTag("00401102"), ActionCodes.REMOVE),  # PersonAddress
        (SingleTag("00401104"), ActionCodes.REMOVE),  # PersonTelecomInformation
        (SingleTag("00401103"), ActionCodes.REMOVE),  # PersonTelephoneNumbers
        (SingleTag("00401101"), ActionCodes.DUMMY),  # PersonIdentificationCodeSequence
        (SingleTag("0040a123"), ActionCodes.DUMMY),  # PersonName
        (SingleTag("00081048"), ActionCodes.REMOVE),  # PhysiciansOfRecord
        (
            SingleTag("00081049"),
            ActionCodes.REMOVE,
        ),  # PhysiciansOfRecordIdentificationSequence
        (
            SingleTag("00081062"),
            ActionCodes.REMOVE,
        ),  # PhysiciansReadingStudyIdentificationSequence
        (SingleTag("40080114"), ActionCodes.REMOVE),  # PhysicianApprovingInterpretation
        (
            SingleTag("00402016"),
            ActionCodes.EMPTY,
        ),  # PlacerOrderNumberImagingServiceRequest
        (SingleTag("00181004"), ActionCodes.REMOVE),  # PlateID
        (SingleTag("001021c0"), ActionCodes.REMOVE),  # PregnancyStatus
        (SingleTag("00400012"), ActionCodes.REMOVE),  # PreMedication
        (SingleTag("300a000e"), ActionCodes.REMOVE),  # PrescriptionDescription
        (SingleTag("3010007b"), ActionCodes.EMPTY),  # PrescriptionNotes
        (SingleTag("30100081"), ActionCodes.EMPTY),  # PrescriptionNotesSequence
        (SingleTag("00701101"), ActionCodes.UID),  # PresentationDisplayCollectionUID
        (SingleTag("00701102"), ActionCodes.UID),  # PresentationSequenceCollectionUID
        (SingleTag("30100061"), ActionCodes.REMOVE),  # PriorTreatmentDoseDescription
        (PrivateTags(), ActionCodes.REMOVE),  # Private Attributes
        (
            SingleTag("00404052"),
            ActionCodes.REMOVE,
        ),  # ProcedureStepCancellationDateTime
        (SingleTag("00181030"), ActionCodes.REMOVE_OR_DUMMY),  # ProtocolName
        (SingleTag("300a0619"), ActionCodes.DUMMY),  # RadiationDoseIdentificationLabel
        (
            SingleTag("300a0623"),
            ActionCodes.DUMMY,
        ),  # RadiationDoseInVivoMeasurementLabel
        (
            SingleTag("300a067d"),
            ActionCodes.EMPTY,
        ),  # RadiationGenerationModeDescription
        (SingleTag("300a067c"), ActionCodes.DUMMY),  # RadiationGenerationModeLabel
        (SingleTag("300c0113"), ActionCodes.REMOVE),  # ReasonForOmissionDescription
        (
            SingleTag("0040100a"),
            ActionCodes.REMOVE,
        ),  # ReasonForRequestedProcedureCodeSequence
        (SingleTag("00321030"), ActionCodes.REMOVE),  # ReasonForStudy
        (SingleTag("3010005c"), ActionCodes.EMPTY),  # ReasonForSuperseding
        (
            SingleTag("00402001"),
            ActionCodes.REMOVE,
        ),  # ReasonForTheImagingServiceRequest
        (SingleTag("00401002"), ActionCodes.REMOVE),  # ReasonForTheRequestedProcedure
        (SingleTag("00321066"), ActionCodes.REMOVE),  # ReasonForVisit
        (SingleTag("00321067"), ActionCodes.REMOVE),  # ReasonForVisitCodeSequence
        (SingleTag("300a073a"), ActionCodes.DUMMY),  # Unknown Tag
        (SingleTag("3010000b"), ActionCodes.UID),  # ReferencedConceptualVolumeUID
        (
            SingleTag("04000402"),
            ActionCodes.REMOVE,
        ),  # ReferencedDigitalSignatureSequence
        (SingleTag("300a0083"), ActionCodes.UID),  # ReferencedDoseReferenceUID
        (SingleTag("3010006f"), ActionCodes.UID),  # ReferencedDosimetricObjectiveUID
        (SingleTag("30100031"), ActionCodes.UID),  # ReferencedFiducialsUID
        (SingleTag("30060024"), ActionCodes.UID),  # ReferencedFrameOfReferenceUID
        (
            SingleTag("00404023"),
            ActionCodes.UID,
        ),  # ReferencedGeneralPurposeScheduledProcedureStepTransactionUID
        (
            SingleTag("00081140"),
            ActionCodes.REMOVE_OR_EMPTY_OR_UID,
        ),  # ReferencedImageSequence
        (SingleTag("0040a172"), ActionCodes.UID),  # ReferencedObservationUIDTrial
        (SingleTag("00380004"), ActionCodes.REMOVE),  # ReferencedPatientAliasSequence
        (SingleTag("00101100"), ActionCodes.REMOVE),  # ReferencedPatientPhotoSequence
        (SingleTag("00081120"), ActionCodes.REMOVE),  # ReferencedPatientSequence
        (
            SingleTag("00081111"),
            ActionCodes.REMOVE_OR_EMPTY_OR_DUMMY,
        ),  # ReferencedPerformedProcedureStepSequence
        (SingleTag("04000403"), ActionCodes.REMOVE),  # ReferencedSOPInstanceMACSequence
        (SingleTag("00081155"), ActionCodes.UID),  # ReferencedSOPInstanceUID
        (SingleTag("00041511"), ActionCodes.UID),  # ReferencedSOPInstanceUIDInFile
        (SingleTag("00081110"), ActionCodes.REMOVE_OR_EMPTY),  # ReferencedStudySequence
        (SingleTag("00080092"), ActionCodes.REMOVE),  # ReferringPhysicianAddress
        (SingleTag("00080090"), ActionCodes.EMPTY),  # ReferringPhysicianName
        (
            SingleTag("00080094"),
            ActionCodes.REMOVE,
        ),  # ReferringPhysicianTelephoneNumbers
        (
            SingleTag("00080096"),
            ActionCodes.REMOVE,
        ),  # ReferringPhysicianIdentificationSequence
        (SingleTag("00102152"), ActionCodes.REMOVE),  # RegionOfResidence
        (SingleTag("300600c2"), ActionCodes.UID),  # RelatedFrameOfReferenceUID
        (SingleTag("00400275"), ActionCodes.REMOVE),  # RequestAttributesSequence
        (SingleTag("00321070"), ActionCodes.REMOVE),  # RequestedContrastAgent
        (SingleTag("00401400"), ActionCodes.REMOVE),  # RequestedProcedureComments
        (
            SingleTag("00321060"),
            ActionCodes.REMOVE_OR_EMPTY,
        ),  # RequestedProcedureDescription
        (SingleTag("00401001"), ActionCodes.REMOVE),  # RequestedProcedureID
        (SingleTag("00401005"), ActionCodes.REMOVE),  # RequestedProcedureLocation
        (SingleTag("00001001"), ActionCodes.UID),  # RequestedSOPInstanceUID
        (SingleTag("00321032"), ActionCodes.REMOVE),  # RequestingPhysician
        (SingleTag("00321033"), ActionCodes.REMOVE),  # RequestingService
        (
            SingleTag("00189185"),
            ActionCodes.REMOVE,
        ),  # RespiratoryMotionCompensationTechniqueDescription
        (SingleTag("00102299"), ActionCodes.REMOVE),  # ResponsibleOrganization
        (SingleTag("00102297"), ActionCodes.REMOVE),  # ResponsiblePerson
        (SingleTag("40084000"), ActionCodes.REMOVE),  # ResultsComments
        (SingleTag("40080118"), ActionCodes.REMOVE),  # ResultsDistributionListSequence
        (SingleTag("40080042"), ActionCodes.REMOVE),  # ResultsIDIssuer
        (SingleTag("300e0008"), ActionCodes.REMOVE_OR_EMPTY),  # ReviewerName
        (SingleTag("300a0615"), ActionCodes.EMPTY),  # RTAccessoryDeviceSlotID
        (SingleTag("300a0611"), ActionCodes.EMPTY),  # RTAccessoryHolderSlotID
        (SingleTag("3010005a"), ActionCodes.EMPTY),  # RTPhysicianIntentNarrative
        (SingleTag("300a0006"), ActionCodes.REMOVE_OR_DUMMY),  # RTPlanDate
        (SingleTag("300a0004"), ActionCodes.REMOVE),  # RTPlanDescription
        (SingleTag("300a0002"), ActionCodes.DUMMY),  # RTPlanLabel
        (SingleTag("300a0003"), ActionCodes.REMOVE),  # RTPlanName
        (SingleTag("300a0007"), ActionCodes.REMOVE_OR_DUMMY),  # RTPlanTime
        (SingleTag("30100054"), ActionCodes.DUMMY),  # RTPrescriptionLabel
        (SingleTag("300a062a"), ActionCodes.DUMMY),  # RTToleranceSetLabel
        (
            SingleTag("30100056"),
            ActionCodes.REMOVE_OR_DUMMY,
        ),  # RTTreatmentApproachLabel
        (SingleTag("3010003b"), ActionCodes.UID),  # RTTreatmentPhaseUID
        (SingleTag("00404034"), ActionCodes.REMOVE),  # ScheduledHumanPerformersSequence
        (
            SingleTag("0038001e"),
            ActionCodes.REMOVE,
        ),  # ScheduledPatientInstitutionResidence
        (SingleTag("00400006"), ActionCodes.REMOVE),  # ScheduledPerformingPhysicianName
        (
            SingleTag("0040000b"),
            ActionCodes.REMOVE,
        ),  # ScheduledPerformingPhysicianIdentificationSequence
        (
            SingleTag("00400007"),
            ActionCodes.REMOVE,
        ),  # ScheduledProcedureStepDescription
        (SingleTag("00400004"), ActionCodes.REMOVE),  # ScheduledProcedureStepEndDate
        (SingleTag("00400005"), ActionCodes.REMOVE),  # ScheduledProcedureStepEndTime
        (
            SingleTag("00404008"),
            ActionCodes.REMOVE,
        ),  # ScheduledProcedureStepExpirationDateTime
        (SingleTag("00400011"), ActionCodes.REMOVE),  # ScheduledProcedureStepLocation
        (
            SingleTag("00404010"),
            ActionCodes.REMOVE,
        ),  # ScheduledProcedureStepModificationDateTime
        (SingleTag("00400002"), ActionCodes.REMOVE),  # ScheduledProcedureStepStartDate
        (
            SingleTag("00404005"),
            ActionCodes.REMOVE,
        ),  # ScheduledProcedureStepStartDateTime
        (SingleTag("00400003"), ActionCodes.REMOVE),  # ScheduledProcedureStepStartTime
        (SingleTag("00400001"), ActionCodes.REMOVE),  # ScheduledStationAETitle
        (
            SingleTag("00404027"),
            ActionCodes.REMOVE,
        ),  # ScheduledStationGeographicLocationCodeSequence
        (SingleTag("00400010"), ActionCodes.REMOVE),  # ScheduledStationName
        (SingleTag("00404025"), ActionCodes.REMOVE),  # ScheduledStationNameCodeSequence
        (SingleTag("00321020"), ActionCodes.REMOVE),  # ScheduledStudyLocation
        (SingleTag("00321021"), ActionCodes.REMOVE),  # ScheduledStudyLocationAETitle
        (SingleTag("00080021"), ActionCodes.REMOVE_OR_DUMMY),  # SeriesDate
        (SingleTag("0008103e"), ActionCodes.REMOVE),  # SeriesDescription
        (SingleTag("0020000e"), ActionCodes.UID),  # SeriesInstanceUID
        (SingleTag("00080031"), ActionCodes.REMOVE_OR_DUMMY),  # SeriesTime
        (SingleTag("00380062"), ActionCodes.REMOVE),  # ServiceEpisodeDescription
        (SingleTag("00380060"), ActionCodes.REMOVE),  # ServiceEpisodeID
        (SingleTag("300a01b2"), ActionCodes.REMOVE),  # SetupTechniqueDescription
        (SingleTag("300a01a6"), ActionCodes.REMOVE),  # ShieldingDeviceDescription
        (SingleTag("004006fa"), ActionCodes.REMOVE),  # SlideIdentifier
        (SingleTag("001021a0"), ActionCodes.REMOVE),  # SmokingStatus
        (SingleTag("00080018"), ActionCodes.UID),  # SOPInstanceUID
        (SingleTag("30100015"), ActionCodes.UID),  # SourceConceptualVolumeUID
        (SingleTag("0018936a"), ActionCodes.DUMMY),  # SourceEndDateTime
        (SingleTag("00340005"), ActionCodes.DUMMY),  # SourceIdentifier
        (
            SingleTag("00082112"),
            ActionCodes.REMOVE_OR_EMPTY_OR_UID,
        ),  # SourceImageSequence
        (SingleTag("300a0216"), ActionCodes.REMOVE),  # SourceManufacturer
        (SingleTag("30080105"), ActionCodes.REMOVE_OR_EMPTY),  # SourceSerialNumber
        (SingleTag("00189369"), ActionCodes.DUMMY),  # SourceStartDateTime
        (SingleTag("00380050"), ActionCodes.REMOVE),  # SpecialNeeds
        (SingleTag("0040050a"), ActionCodes.REMOVE),  # SpecimenAccessionNumber
        (SingleTag("00400602"), ActionCodes.REMOVE),  # SpecimenDetailedDescription
        (SingleTag("00400551"), ActionCodes.DUMMY),  # SpecimenIdentifier
        (SingleTag("00400610"), ActionCodes.EMPTY),  # SpecimenPreparationSequence
        (SingleTag("00400600"), ActionCodes.REMOVE),  # SpecimenShortDescription
        (SingleTag("00400554"), ActionCodes.UID),  # SpecimenUID
        (
            SingleTag("00189516"),
            ActionCodes.REMOVE_OR_DUMMY,
        ),  # StartAcquisitionDateTime
        (SingleTag("00081010"), ActionCodes.REMOVE_OR_EMPTY_OR_DUMMY),  # StationName
        (SingleTag("00880140"), ActionCodes.UID),  # StorageMediaFileSetUID
        (SingleTag("00324000"), ActionCodes.REMOVE),  # StudyComments
        (SingleTag("00080020"), ActionCodes.EMPTY),  # StudyDate
        (SingleTag("00081030"), ActionCodes.REMOVE),  # StudyDescription
        (SingleTag("00200010"), ActionCodes.EMPTY),  # StudyID
        (SingleTag("00320012"), ActionCodes.REMOVE),  # StudyIDIssuer
        (SingleTag("0020000d"), ActionCodes.UID),  # StudyInstanceUID
        (SingleTag("00080030"), ActionCodes.EMPTY),  # StudyTime
        (SingleTag("00200200"), ActionCodes.UID),  # SynchronizationFrameOfReferenceUID
        (SingleTag("00182042"), ActionCodes.UID),  # TargetUID
        (SingleTag("0040a354"), ActionCodes.REMOVE),  # TelephoneNumberTrial
        (SingleTag("0040db0d"), ActionCodes.UID),  # TemplateExtensionCreatorUID
        (SingleTag("0040db0c"), ActionCodes.UID),  # TemplateExtensionOrganizationUID
        (SingleTag("40004000"), ActionCodes.REMOVE),  # TextComments
        (SingleTag("20300020"), ActionCodes.REMOVE),  # TextString
        (SingleTag("00080201"), ActionCodes.REMOVE),  # TimezoneOffsetFromUTC
        (SingleTag("00880910"), ActionCodes.REMOVE),  # TopicAuthor
        (SingleTag("00880912"), ActionCodes.REMOVE),  # TopicKeywords
        (SingleTag("00880906"), ActionCodes.REMOVE),  # TopicSubject
        (SingleTag("00880904"), ActionCodes.REMOVE),  # TopicTitle
        (SingleTag("00620021"), ActionCodes.UID),  # TrackingUID
        (SingleTag("00081195"), ActionCodes.UID),  # TransactionUID
        (SingleTag("30080250"), ActionCodes.REMOVE_OR_DUMMY),  # TreatmentDate
        (SingleTag("300a00b2"), ActionCodes.REMOVE),  # TreatmentMachineName
        (SingleTag("300a0608"), ActionCodes.DUMMY),  # TreatmentPositionGroupLabel
        (SingleTag("300a0609"), ActionCodes.UID),  # TreatmentPositionGroupUID
        (SingleTag("300a0700"), ActionCodes.UID),  # Unknown Tag
        (SingleTag("30100077"), ActionCodes.DUMMY),  # TreatmentSite
        (SingleTag("3010007a"), ActionCodes.EMPTY),  # TreatmentTechniqueNotes
        (SingleTag("30080251"), ActionCodes.REMOVE_OR_DUMMY),  # TreatmentTime
        (SingleTag("300a0736"), ActionCodes.DUMMY),  # Unknown Tag
        (SingleTag("300a0734"), ActionCodes.DUMMY),  # Unknown Tag
        (SingleTag("0018100a"), ActionCodes.REMOVE),  # UDISequence
        (SingleTag("0040a124"), ActionCodes.UID),  # UID
        (SingleTag("00181009"), ActionCodes.REMOVE),  # UniqueDeviceIdentifier
        (SingleTag("30100033"), ActionCodes.DUMMY),  # UserContentLabel
        (SingleTag("30100034"), ActionCodes.DUMMY),  # UserContentLongLabel
        (SingleTag("0040a352"), ActionCodes.REMOVE),  # VerbalSourceTrial
        (
            SingleTag("0040a358"),
            ActionCodes.REMOVE,
        ),  # VerbalSourceIdentifierCodeSequenceTrial
        (
            SingleTag("0040a088"),
            ActionCodes.EMPTY,
        ),  # VerifyingObserverIdentificationCodeSequence
        (SingleTag("0040a075"), ActionCodes.DUMMY),  # VerifyingObserverName
        (SingleTag("0040a073"), ActionCodes.DUMMY),  # VerifyingObserverSequence
        (SingleTag("0040a027"), ActionCodes.DUMMY),  # VerifyingOrganization
        (SingleTag("00384000"), ActionCodes.REMOVE),  # VisitComments
        (SingleTag("00189371"), ActionCodes.DUMMY),  # XRayDetectorID
        (SingleTag("00189373"), ActionCodes.REMOVE),  # XRayDetectorLabel
        (SingleTag("00189367"), ActionCodes.DUMMY),  # XRaySourceID
    ],
)

retain_safe_private = RawNemaRuleSet(
    name="Retain Safe Private Option",
    code="113111",
    rules=[(PrivateTags(), ActionCodes.CLEAN)],  # Private Attributes
)

retain_uid = RawNemaRuleSet(
    name="Retain UIDs",
    code="113110",
    rules=[
        (SingleTag("00001000"), ActionCodes.KEEP),  # AffectedSOPInstanceUID
        (SingleTag("00209161"), ActionCodes.KEEP),  # ConcatenationUID
        (SingleTag("30100006"), ActionCodes.KEEP),  # ConceptualVolumeUID
        (SingleTag("30100013"), ActionCodes.KEEP),  # ConstituentConceptualVolumeUID
        (SingleTag("00181002"), ActionCodes.KEEP),  # DeviceUID
        (SingleTag("00209164"), ActionCodes.KEEP),  # DimensionOrganizationUID
        (SingleTag("300a0013"), ActionCodes.KEEP),  # DoseReferenceUID
        (SingleTag("3010006e"), ActionCodes.KEEP),  # DosimetricObjectiveUID
        (SingleTag("00080058"), ActionCodes.KEEP),  # FailedSOPInstanceUIDList
        (SingleTag("0070031a"), ActionCodes.KEEP),  # FiducialUID
        (SingleTag("00200052"), ActionCodes.KEEP),  # FrameOfReferenceUID
        (SingleTag("00080014"), ActionCodes.KEEP),  # InstanceCreatorUID
        (SingleTag("00083010"), ActionCodes.KEEP),  # IrradiationEventUID
        (SingleTag("00281214"), ActionCodes.KEEP),  # LargePaletteColorLookupTableUID
        (SingleTag("0018100b"), ActionCodes.KEEP),  # ManufacturerDeviceClassUID
        (SingleTag("00020003"), ActionCodes.KEEP),  # MediaStorageSOPInstanceUID
        (SingleTag("003a0310"), ActionCodes.KEEP),  # Unknown Tag
        (SingleTag("0040a402"), ActionCodes.KEEP),  # ObservationSubjectUIDTrial
        (SingleTag("0040a171"), ActionCodes.KEEP),  # ObservationUID
        (SingleTag("00281199"), ActionCodes.KEEP),  # PaletteColorLookupTableUID
        (SingleTag("300a0650"), ActionCodes.KEEP),  # PatientSetupUID
        (SingleTag("00701101"), ActionCodes.KEEP),  # PresentationDisplayCollectionUID
        (SingleTag("00701102"), ActionCodes.KEEP),  # PresentationSequenceCollectionUID
        (SingleTag("3010000b"), ActionCodes.KEEP),  # ReferencedConceptualVolumeUID
        (SingleTag("300a0083"), ActionCodes.KEEP),  # ReferencedDoseReferenceUID
        (SingleTag("3010006f"), ActionCodes.KEEP),  # ReferencedDosimetricObjectiveUID
        (SingleTag("30100031"), ActionCodes.KEEP),  # ReferencedFiducialsUID
        (SingleTag("30060024"), ActionCodes.KEEP),  # ReferencedFrameOfReferenceUID
        (
            SingleTag("00404023"),
            ActionCodes.KEEP,
        ),  # ReferencedGeneralPurposeScheduledProcedureStepTransactionUID
        (SingleTag("00081140"), ActionCodes.KEEP),  # ReferencedImageSequence
        (SingleTag("0040a172"), ActionCodes.KEEP),  # ReferencedObservationUIDTrial
        (SingleTag("00081120"), ActionCodes.REMOVE),  # ReferencedPatientSequence
        (
            SingleTag("00081111"),
            ActionCodes.KEEP,
        ),  # ReferencedPerformedProcedureStepSequence
        (SingleTag("00081155"), ActionCodes.KEEP),  # ReferencedSOPInstanceUID
        (SingleTag("00041511"), ActionCodes.KEEP),  # ReferencedSOPInstanceUIDInFile
        (SingleTag("00081110"), ActionCodes.KEEP),  # ReferencedStudySequence
        (SingleTag("300600c2"), ActionCodes.KEEP),  # RelatedFrameOfReferenceUID
        (SingleTag("00001001"), ActionCodes.KEEP),  # RequestedSOPInstanceUID
        (SingleTag("3010003b"), ActionCodes.KEEP),  # RTTreatmentPhaseUID
        (SingleTag("0020000e"), ActionCodes.KEEP),  # SeriesInstanceUID
        (SingleTag("00080018"), ActionCodes.KEEP),  # SOPInstanceUID
        (SingleTag("30100015"), ActionCodes.KEEP),  # SourceConceptualVolumeUID
        (SingleTag("00082112"), ActionCodes.KEEP),  # SourceImageSequence
        (SingleTag("00400554"), ActionCodes.KEEP),  # SpecimenUID
        (SingleTag("00880140"), ActionCodes.KEEP),  # StorageMediaFileSetUID
        (SingleTag("0020000d"), ActionCodes.KEEP),  # StudyInstanceUID
        (SingleTag("00200200"), ActionCodes.KEEP),  # SynchronizationFrameOfReferenceUID
        (SingleTag("00182042"), ActionCodes.KEEP),  # TargetUID
        (SingleTag("0040db0d"), ActionCodes.KEEP),  # TemplateExtensionCreatorUID
        (SingleTag("0040db0c"), ActionCodes.KEEP),  # TemplateExtensionOrganizationUID
        (SingleTag("00620021"), ActionCodes.KEEP),  # TrackingUID
        (SingleTag("00081195"), ActionCodes.KEEP),  # TransactionUID
        (SingleTag("300a0609"), ActionCodes.KEEP),  # TreatmentPositionGroupUID
        (SingleTag("300a0700"), ActionCodes.KEEP),  # Unknown Tag
    ],
)

retain_device_id = RawNemaRuleSet(
    name="Retain Device Identity Option",
    code="113109",
    rules=[
        (SingleTag("00181007"), ActionCodes.KEEP),  # CassetteID
        (SingleTag("0018700a"), ActionCodes.KEEP),  # DetectorID
        (SingleTag("00500020"), ActionCodes.KEEP),  # DeviceDescription
        (SingleTag("3010002d"), ActionCodes.KEEP),  # DeviceLabel
        (SingleTag("00181000"), ActionCodes.KEEP),  # DeviceSerialNumber
        (SingleTag("00181002"), ActionCodes.KEEP),  # DeviceUID
        (SingleTag("00181008"), ActionCodes.KEEP),  # GantryID
        (SingleTag("00181005"), ActionCodes.KEEP),  # GeneratorID
        (SingleTag("0016004f"), ActionCodes.KEEP),  # LensMake
        (SingleTag("00160050"), ActionCodes.KEEP),  # LensModel
        (SingleTag("00160051"), ActionCodes.KEEP),  # LensSerialNumber
        (SingleTag("0016004e"), ActionCodes.KEEP),  # LensSpecification
        (SingleTag("0018100b"), ActionCodes.KEEP),  # ManufacturerDeviceClassUID
        (SingleTag("30100043"), ActionCodes.KEEP),  # ManufacturerDeviceIdentifier
        (SingleTag("00400241"), ActionCodes.KEEP),  # PerformedStationAETitle
        (
            SingleTag("00404030"),
            ActionCodes.KEEP,
        ),  # PerformedStationGeographicLocationCodeSequence
        (SingleTag("00400242"), ActionCodes.KEEP),  # PerformedStationName
        (SingleTag("00404028"), ActionCodes.KEEP),  # PerformedStationNameCodeSequence
        (SingleTag("00181004"), ActionCodes.KEEP),  # PlateID
        (SingleTag("00400011"), ActionCodes.KEEP),  # ScheduledProcedureStepLocation
        (SingleTag("00400001"), ActionCodes.KEEP),  # ScheduledStationAETitle
        (
            SingleTag("00404027"),
            ActionCodes.KEEP,
        ),  # ScheduledStationGeographicLocationCodeSequence
        (SingleTag("00400010"), ActionCodes.KEEP),  # ScheduledStationName
        (SingleTag("00404025"), ActionCodes.KEEP),  # ScheduledStationNameCodeSequence
        (SingleTag("00321020"), ActionCodes.KEEP),  # ScheduledStudyLocation
        (SingleTag("00321021"), ActionCodes.KEEP),  # ScheduledStudyLocationAETitle
        (SingleTag("300a0216"), ActionCodes.KEEP),  # SourceManufacturer
        (SingleTag("30080105"), ActionCodes.KEEP),  # SourceSerialNumber
        (SingleTag("00081010"), ActionCodes.KEEP),  # StationName
        (SingleTag("300a00b2"), ActionCodes.KEEP),  # TreatmentMachineName
        (SingleTag("0018100a"), ActionCodes.KEEP),  # UDISequence
        (SingleTag("00181009"), ActionCodes.KEEP),  # UniqueDeviceIdentifier
        (SingleTag("00189371"), ActionCodes.KEEP),  # XRayDetectorID
        (SingleTag("00189373"), ActionCodes.KEEP),  # XRayDetectorLabel
        (SingleTag("00189367"), ActionCodes.KEEP),  # XRaySourceID
    ],
)

retain_institution_id = RawNemaRuleSet(
    name="Retain Institution Identity Option",
    code="113112",
    rules=[
        (
            SingleTag("00120060"),
            ActionCodes.KEEP,
        ),  # ClinicalTrialCoordinatingCenterName
        (
            SingleTag("00120081"),
            ActionCodes.KEEP,
        ),  # ClinicalTrialProtocolEthicsCommitteeName
        (SingleTag("00120030"), ActionCodes.KEEP),  # ClinicalTrialSiteID
        (SingleTag("00120031"), ActionCodes.KEEP),  # ClinicalTrialSiteName
        (SingleTag("00080081"), ActionCodes.KEEP),  # InstitutionAddress
        (SingleTag("00081040"), ActionCodes.KEEP),  # InstitutionalDepartmentName
        (
            SingleTag("00081041"),
            ActionCodes.KEEP,
        ),  # InstitutionalDepartmentTypeCodeSequence
        (SingleTag("00080082"), ActionCodes.KEEP),  # InstitutionCodeSequence
        (SingleTag("00080080"), ActionCodes.KEEP),  # InstitutionName
    ],
)

retain_patient_characteristics = RawNemaRuleSet(
    name="Retain Patient Characteristics Option",
    code="113108",
    rules=[
        (SingleTag("00102110"), ActionCodes.CLEAN),  # Allergies
        (SingleTag("00102160"), ActionCodes.KEEP),  # EthnicGroup
        (SingleTag("00101010"), ActionCodes.KEEP),  # PatientAge
        (SingleTag("00100040"), ActionCodes.KEEP),  # PatientSex
        (SingleTag("00102203"), ActionCodes.KEEP),  # PatientSexNeutered
        (SingleTag("00101020"), ActionCodes.KEEP),  # PatientSize
        (SingleTag("00101030"), ActionCodes.KEEP),  # PatientWeight
        (SingleTag("00380500"), ActionCodes.CLEAN),  # PatientState
        (SingleTag("001021c0"), ActionCodes.KEEP),  # PregnancyStatus
        (SingleTag("00400012"), ActionCodes.CLEAN),  # PreMedication
        (SingleTag("001021a0"), ActionCodes.KEEP),  # SmokingStatus
        (SingleTag("00380050"), ActionCodes.CLEAN),  # SpecialNeeds
    ],
)

retain_full_dates = RawNemaRuleSet(
    name="Retain Longitudinal Temporal Information with Full Dates Option",
    code="113106",
    rules=[
        (SingleTag("00080022"), ActionCodes.KEEP),  # AcquisitionDate
        (SingleTag("0008002a"), ActionCodes.KEEP),  # AcquisitionDateTime
        (SingleTag("00080032"), ActionCodes.KEEP),  # AcquisitionTime
        (SingleTag("00380020"), ActionCodes.KEEP),  # AdmittingDate
        (SingleTag("00380021"), ActionCodes.KEEP),  # AdmittingTime
        (SingleTag("00080023"), ActionCodes.KEEP),  # ContentDate
        (SingleTag("00080033"), ActionCodes.KEEP),  # ContentTime
        (SingleTag("00080025"), ActionCodes.KEEP),  # CurveDate
        (SingleTag("00080035"), ActionCodes.KEEP),  # CurveTime
        (SingleTag("00189517"), ActionCodes.KEEP),  # EndAcquisitionDateTime
        (SingleTag("00404011"), ActionCodes.KEEP),  # ExpectedCompletionDateTime
        (SingleTag("30080054"), ActionCodes.KEEP),  # FirstTreatmentDate
        (SingleTag("00340007"), ActionCodes.KEEP),  # FrameOriginTimestamp
        (SingleTag("0016008d"), ActionCodes.KEEP),  # GPSDateStamp
        (SingleTag("003a0314"), ActionCodes.KEEP),  # Unknown Tag
        (SingleTag("00080015"), ActionCodes.KEEP),  # InstanceCoercionDateTime
        (SingleTag("3010004d"), ActionCodes.KEEP),  # IntendedPhaseEndDate
        (SingleTag("3010004c"), ActionCodes.KEEP),  # IntendedPhaseStartDate
        (SingleTag("300a0741"), ActionCodes.KEEP),  # Unknown Tag
        (SingleTag("001021d0"), ActionCodes.KEEP),  # LastMenstrualDate
        (SingleTag("30080056"), ActionCodes.KEEP),  # MostRecentTreatmentDate
        (SingleTag("0040a192"), ActionCodes.KEEP),  # ObservationDateTrial
        (SingleTag("0040a193"), ActionCodes.KEEP),  # ObservationTimeTrial
        (SingleTag("00080024"), ActionCodes.KEEP),  # OverlayDate
        (SingleTag("00080034"), ActionCodes.KEEP),  # OverlayTime
        (SingleTag("300a0760"), ActionCodes.KEEP),  # Unknown Tag
        (SingleTag("00400250"), ActionCodes.KEEP),  # PerformedProcedureStepEndDate
        (SingleTag("00404051"), ActionCodes.KEEP),  # PerformedProcedureStepEndDateTime
        (SingleTag("00400251"), ActionCodes.KEEP),  # PerformedProcedureStepEndTime
        (SingleTag("00400244"), ActionCodes.KEEP),  # PerformedProcedureStepStartDate
        (
            SingleTag("00404050"),
            ActionCodes.KEEP,
        ),  # PerformedProcedureStepStartDateTime
        (SingleTag("00400245"), ActionCodes.KEEP),  # PerformedProcedureStepStartTime
        (SingleTag("00404052"), ActionCodes.KEEP),  # ProcedureStepCancellationDateTime
        (SingleTag("300a073a"), ActionCodes.KEEP),  # Unknown Tag
        (SingleTag("300a0006"), ActionCodes.KEEP),  # RTPlanDate
        (SingleTag("300a0007"), ActionCodes.KEEP),  # RTPlanTime
        (SingleTag("00400004"), ActionCodes.KEEP),  # ScheduledProcedureStepEndDate
        (SingleTag("00400005"), ActionCodes.KEEP),  # ScheduledProcedureStepEndTime
        (
            SingleTag("00404008"),
            ActionCodes.KEEP,
        ),  # ScheduledProcedureStepExpirationDateTime
        (
            SingleTag("00404010"),
            ActionCodes.KEEP,
        ),  # ScheduledProcedureStepModificationDateTime
        (SingleTag("00400002"), ActionCodes.KEEP),  # ScheduledProcedureStepStartDate
        (
            SingleTag("00404005"),
            ActionCodes.KEEP,
        ),  # ScheduledProcedureStepStartDateTime
        (SingleTag("00400003"), ActionCodes.KEEP),  # ScheduledProcedureStepStartTime
        (SingleTag("00080021"), ActionCodes.KEEP),  # SeriesDate
        (SingleTag("00080031"), ActionCodes.KEEP),  # SeriesTime
        (SingleTag("0018936a"), ActionCodes.KEEP),  # SourceEndDateTime
        (SingleTag("00189369"), ActionCodes.KEEP),  # SourceStartDateTime
        (SingleTag("00189516"), ActionCodes.KEEP),  # StartAcquisitionDateTime
        (SingleTag("00080020"), ActionCodes.KEEP),  # StudyDate
        (SingleTag("00080030"), ActionCodes.KEEP),  # StudyTime
        (SingleTag("00080201"), ActionCodes.KEEP),  # TimezoneOffsetFromUTC
        (SingleTag("30080250"), ActionCodes.KEEP),  # TreatmentDate
        (SingleTag("30080251"), ActionCodes.KEEP),  # TreatmentTime
        (SingleTag("300a0736"), ActionCodes.KEEP),  # Unknown Tag
    ],
)

retain_modified_dates = RawNemaRuleSet(
    name="Retain Longitudinal Temporal Information with Modified Dates Option",
    code="113107",
    rules=[
        (SingleTag("00080022"), ActionCodes.CLEAN),  # AcquisitionDate
        (SingleTag("0008002a"), ActionCodes.CLEAN),  # AcquisitionDateTime
        (SingleTag("00080032"), ActionCodes.CLEAN),  # AcquisitionTime
        (SingleTag("00380020"), ActionCodes.CLEAN),  # AdmittingDate
        (SingleTag("00380021"), ActionCodes.CLEAN),  # AdmittingTime
        (SingleTag("00080023"), ActionCodes.CLEAN),  # ContentDate
        (SingleTag("00080033"), ActionCodes.CLEAN),  # ContentTime
        (SingleTag("00080025"), ActionCodes.CLEAN),  # CurveDate
        (SingleTag("00080035"), ActionCodes.CLEAN),  # CurveTime
        (SingleTag("00189517"), ActionCodes.CLEAN),  # EndAcquisitionDateTime
        (SingleTag("00404011"), ActionCodes.CLEAN),  # ExpectedCompletionDateTime
        (SingleTag("30080054"), ActionCodes.CLEAN),  # FirstTreatmentDate
        (SingleTag("00340007"), ActionCodes.CLEAN),  # FrameOriginTimestamp
        (SingleTag("0016008d"), ActionCodes.CLEAN),  # GPSDateStamp
        (SingleTag("003a0314"), ActionCodes.CLEAN),  # Unknown Tag
        (SingleTag("00080015"), ActionCodes.CLEAN),  # InstanceCoercionDateTime
        (SingleTag("3010004d"), ActionCodes.CLEAN),  # IntendedPhaseEndDate
        (SingleTag("3010004c"), ActionCodes.CLEAN),  # IntendedPhaseStartDate
        (SingleTag("300a0741"), ActionCodes.CLEAN),  # Unknown Tag
        (SingleTag("001021d0"), ActionCodes.CLEAN),  # LastMenstrualDate
        (SingleTag("30080056"), ActionCodes.CLEAN),  # MostRecentTreatmentDate
        (SingleTag("0040a192"), ActionCodes.CLEAN),  # ObservationDateTrial
        (SingleTag("0040a193"), ActionCodes.CLEAN),  # ObservationTimeTrial
        (SingleTag("00080024"), ActionCodes.CLEAN),  # OverlayDate
        (SingleTag("00080034"), ActionCodes.CLEAN),  # OverlayTime
        (SingleTag("300a0760"), ActionCodes.CLEAN),  # Unknown Tag
        (SingleTag("00400250"), ActionCodes.CLEAN),  # PerformedProcedureStepEndDate
        (SingleTag("00404051"), ActionCodes.CLEAN),  # PerformedProcedureStepEndDateTime
        (SingleTag("00400251"), ActionCodes.CLEAN),  # PerformedProcedureStepEndTime
        (SingleTag("00400244"), ActionCodes.CLEAN),  # PerformedProcedureStepStartDate
        (
            SingleTag("00404050"),
            ActionCodes.CLEAN,
        ),  # PerformedProcedureStepStartDateTime
        (SingleTag("00400245"), ActionCodes.CLEAN),  # PerformedProcedureStepStartTime
        (SingleTag("00404052"), ActionCodes.CLEAN),  # ProcedureStepCancellationDateTime
        (SingleTag("300a073a"), ActionCodes.CLEAN),  # Unknown Tag
        (SingleTag("300a0006"), ActionCodes.CLEAN),  # RTPlanDate
        (SingleTag("300a0007"), ActionCodes.CLEAN),  # RTPlanTime
        (SingleTag("00400004"), ActionCodes.CLEAN),  # ScheduledProcedureStepEndDate
        (SingleTag("00400005"), ActionCodes.CLEAN),  # ScheduledProcedureStepEndTime
        (
            SingleTag("00404008"),
            ActionCodes.CLEAN,
        ),  # ScheduledProcedureStepExpirationDateTime
        (
            SingleTag("00404010"),
            ActionCodes.CLEAN,
        ),  # ScheduledProcedureStepModificationDateTime
        (SingleTag("00400002"), ActionCodes.CLEAN),  # ScheduledProcedureStepStartDate
        (
            SingleTag("00404005"),
            ActionCodes.CLEAN,
        ),  # ScheduledProcedureStepStartDateTime
        (SingleTag("00400003"), ActionCodes.CLEAN),  # ScheduledProcedureStepStartTime
        (SingleTag("00080021"), ActionCodes.CLEAN),  # SeriesDate
        (SingleTag("00080031"), ActionCodes.CLEAN),  # SeriesTime
        (SingleTag("0018936a"), ActionCodes.CLEAN),  # SourceEndDateTime
        (SingleTag("00189369"), ActionCodes.CLEAN),  # SourceStartDateTime
        (SingleTag("00189516"), ActionCodes.CLEAN),  # StartAcquisitionDateTime
        (SingleTag("00080020"), ActionCodes.CLEAN),  # StudyDate
        (SingleTag("00080030"), ActionCodes.CLEAN),  # StudyTime
        (SingleTag("00080201"), ActionCodes.CLEAN),  # TimezoneOffsetFromUTC
        (SingleTag("30080250"), ActionCodes.CLEAN),  # TreatmentDate
        (SingleTag("30080251"), ActionCodes.CLEAN),  # TreatmentTime
        (SingleTag("300a0736"), ActionCodes.CLEAN),  # Unknown Tag
    ],
)

clean_descriptors = RawNemaRuleSet(
    name="Clean Descriptors Option",
    code="113105",
    rules=[
        (SingleTag("00184000"), ActionCodes.CLEAN),  # AcquisitionComments
        (
            SingleTag("00181400"),
            ActionCodes.CLEAN,
        ),  # AcquisitionDeviceProcessingDescription
        (SingleTag("00189424"), ActionCodes.CLEAN),  # AcquisitionProtocolDescription
        (SingleTag("001021b0"), ActionCodes.CLEAN),  # AdditionalPatientHistory
        (SingleTag("00081084"), ActionCodes.CLEAN),  # AdmittingDiagnosesCodeSequence
        (SingleTag("00081080"), ActionCodes.CLEAN),  # AdmittingDiagnosesDescription
        (SingleTag("00102110"), ActionCodes.CLEAN),  # Allergies
        (SingleTag("300a00c3"), ActionCodes.CLEAN),  # BeamDescription
        (SingleTag("300a00dd"), ActionCodes.CLEAN),  # BolusDescription
        (SingleTag("00120072"), ActionCodes.CLEAN),  # ClinicalTrialSeriesDescription
        (SingleTag("00120051"), ActionCodes.CLEAN),  # ClinicalTrialTimePointDescription
        (
            SingleTag("00400280"),
            ActionCodes.CLEAN,
        ),  # CommentsOnThePerformedProcedureStep
        (SingleTag("300a02eb"), ActionCodes.CLEAN),  # CompensatorDescription
        (
            SingleTag("3010000f"),
            ActionCodes.CLEAN,
        ),  # ConceptualVolumeCombinationDescription
        (SingleTag("30100017"), ActionCodes.CLEAN),  # ConceptualVolumeDescription
        (SingleTag("0040051a"), ActionCodes.CLEAN),  # ContainerDescription
        (SingleTag("00180010"), ActionCodes.CLEAN),  # ContrastBolusAgent
        (SingleTag("0018a003"), ActionCodes.CLEAN),  # ContributionDescription
        (SingleTag("0018937f"), ActionCodes.CLEAN),  # DecompositionDescription
        (SingleTag("00082111"), ActionCodes.CLEAN),  # DerivationDescription
        (SingleTag("0016004b"), ActionCodes.CLEAN),  # DeviceSettingDescription
        (SingleTag("00380040"), ActionCodes.CLEAN),  # DischargeDiagnosisDescription
        (SingleTag("300a0016"), ActionCodes.CLEAN),  # DoseReferenceDescription
        (SingleTag("30100037"), ActionCodes.CLEAN),  # EntityDescription
        (SingleTag("30100035"), ActionCodes.CLEAN),  # EntityLabel
        (SingleTag("30100038"), ActionCodes.CLEAN),  # EntityLongLabel
        (SingleTag("30100036"), ActionCodes.CLEAN),  # EntityName
        (
            SingleTag("300a0676"),
            ActionCodes.CLEAN,
        ),  # EquipmentFrameOfReferenceDescription
        (SingleTag("300a0196"), ActionCodes.CLEAN),  # FixationDeviceDescription
        (SingleTag("3010007f"), ActionCodes.CLEAN),  # FractionationNotes
        (SingleTag("300a0072"), ActionCodes.CLEAN),  # FractionGroupDescription
        (SingleTag("00209158"), ActionCodes.CLEAN),  # FrameComments
        (SingleTag("00084000"), ActionCodes.CLEAN),  # IdentifyingComments
        (SingleTag("00204000"), ActionCodes.CLEAN),  # ImageComments
        (SingleTag("00402400"), ActionCodes.CLEAN),  # ImagingServiceRequestComments
        (SingleTag("40080300"), ActionCodes.CLEAN),  # Impressions
        (SingleTag("300a0742"), ActionCodes.CLEAN),  # Unknown Tag
        (SingleTag("300a0783"), ActionCodes.CLEAN),  # Unknown Tag
        (
            SingleTag("40080115"),
            ActionCodes.CLEAN,
        ),  # InterpretationDiagnosisDescription
        (SingleTag("4008010b"), ActionCodes.CLEAN),  # InterpretationText
        (SingleTag("22000002"), ActionCodes.CLEAN),  # LabelText
        (SingleTag("00500021"), ActionCodes.CLEAN),  # LongDeviceDescription
        (SingleTag("0016002b"), ActionCodes.CLEAN),  # MakerNote
        (SingleTag("00102000"), ActionCodes.CLEAN),  # MedicalAlerts
        (SingleTag("0018937b"), ActionCodes.CLEAN),  # MultienergyAcquisitionDescription
        (SingleTag("00102180"), ActionCodes.CLEAN),  # Occupation
        (SingleTag("00104000"), ActionCodes.CLEAN),  # PatientComments
        (SingleTag("00380500"), ActionCodes.CLEAN),  # PatientState
        (SingleTag("00400254"), ActionCodes.CLEAN),  # PerformedProcedureStepDescription
        (SingleTag("300a000e"), ActionCodes.CLEAN),  # PrescriptionDescription
        (SingleTag("3010007b"), ActionCodes.CLEAN),  # PrescriptionNotes
        (SingleTag("30100081"), ActionCodes.CLEAN),  # PrescriptionNotesSequence
        (SingleTag("30100061"), ActionCodes.CLEAN),  # PriorTreatmentDoseDescription
        (SingleTag("00181030"), ActionCodes.CLEAN),  # ProtocolName
        (SingleTag("300a0619"), ActionCodes.CLEAN),  # RadiationDoseIdentificationLabel
        (
            SingleTag("300a0623"),
            ActionCodes.CLEAN,
        ),  # RadiationDoseInVivoMeasurementLabel
        (
            SingleTag("300a067d"),
            ActionCodes.CLEAN,
        ),  # RadiationGenerationModeDescription
        (SingleTag("300a067c"), ActionCodes.CLEAN),  # RadiationGenerationModeLabel
        (SingleTag("300c0113"), ActionCodes.CLEAN),  # ReasonForOmissionDescription
        (
            SingleTag("0040100a"),
            ActionCodes.CLEAN,
        ),  # ReasonForRequestedProcedureCodeSequence
        (SingleTag("00321030"), ActionCodes.CLEAN),  # ReasonForStudy
        (SingleTag("3010005c"), ActionCodes.CLEAN),  # ReasonForSuperseding
        (SingleTag("00402001"), ActionCodes.CLEAN),  # ReasonForTheImagingServiceRequest
        (SingleTag("00401002"), ActionCodes.CLEAN),  # ReasonForTheRequestedProcedure
        (SingleTag("00321066"), ActionCodes.CLEAN),  # ReasonForVisit
        (SingleTag("00321067"), ActionCodes.CLEAN),  # ReasonForVisitCodeSequence
        (SingleTag("00400275"), ActionCodes.CLEAN),  # RequestAttributesSequence
        (SingleTag("00321070"), ActionCodes.CLEAN),  # RequestedContrastAgent
        (SingleTag("00401400"), ActionCodes.CLEAN),  # RequestedProcedureComments
        (SingleTag("00321060"), ActionCodes.CLEAN),  # RequestedProcedureDescription
        (
            SingleTag("00189185"),
            ActionCodes.CLEAN,
        ),  # RespiratoryMotionCompensationTechniqueDescription
        (SingleTag("40084000"), ActionCodes.CLEAN),  # ResultsComments
        (SingleTag("3010005a"), ActionCodes.CLEAN),  # RTPhysicianIntentNarrative
        (SingleTag("300a0004"), ActionCodes.CLEAN),  # RTPlanDescription
        (SingleTag("300a0002"), ActionCodes.CLEAN),  # RTPlanLabel
        (SingleTag("300a0003"), ActionCodes.CLEAN),  # RTPlanName
        (SingleTag("30100054"), ActionCodes.CLEAN),  # RTPrescriptionLabel
        (SingleTag("300a062a"), ActionCodes.CLEAN),  # RTToleranceSetLabel
        (SingleTag("30100056"), ActionCodes.CLEAN),  # RTTreatmentApproachLabel
        (SingleTag("00400007"), ActionCodes.CLEAN),  # ScheduledProcedureStepDescription
        (SingleTag("0008103e"), ActionCodes.CLEAN),  # SeriesDescription
        (SingleTag("00380062"), ActionCodes.CLEAN),  # ServiceEpisodeDescription
        (SingleTag("300a01b2"), ActionCodes.CLEAN),  # SetupTechniqueDescription
        (SingleTag("300a01a6"), ActionCodes.CLEAN),  # ShieldingDeviceDescription
        (SingleTag("00400602"), ActionCodes.CLEAN),  # SpecimenDetailedDescription
        (SingleTag("00400600"), ActionCodes.CLEAN),  # SpecimenShortDescription
        (SingleTag("00324000"), ActionCodes.CLEAN),  # StudyComments
        (SingleTag("00081030"), ActionCodes.CLEAN),  # StudyDescription
        (SingleTag("300a0608"), ActionCodes.CLEAN),  # TreatmentPositionGroupLabel
        (SingleTag("30100077"), ActionCodes.CLEAN),  # TreatmentSite
        (SingleTag("3010007a"), ActionCodes.CLEAN),  # TreatmentTechniqueNotes
        (SingleTag("300a0734"), ActionCodes.CLEAN),  # Unknown Tag
        (SingleTag("30100033"), ActionCodes.CLEAN),  # UserContentLabel
        (SingleTag("30100034"), ActionCodes.CLEAN),  # UserContentLongLabel
        (SingleTag("00384000"), ActionCodes.CLEAN),  # VisitComments
    ],
)

clean_structured_content = RawNemaRuleSet(
    name="Clean Structured Content Option",
    code="113104",
    rules=[
        (SingleTag("00400555"), ActionCodes.CLEAN),  # AcquisitionContextSequence
        (SingleTag("0040a730"), ActionCodes.CLEAN),  # ContentSequence
        (SingleTag("00400610"), ActionCodes.CLEAN),  # SpecimenPreparationSequence
    ],
)

clean_graphics = RawNemaRuleSet(
    name="Clean Graphics Option",
    code="113103",
    rules=[
        (
            RepeatingGroup("50xxxxxx"),
            ActionCodes.CLEAN,
        ),  # Unknown Repeater tag 50xxxxxx
        (SingleTag("00700001"), ActionCodes.CLEAN),  # GraphicAnnotationSequence
        (RepeatingGroup("60xx4000"), ActionCodes.CLEAN),  # OverlayComments
        (RepeatingGroup("60xx3000"), ActionCodes.CLEAN),  # OverlayData
    ],
)
