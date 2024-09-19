"""Public DICOM information auto-generated from generate_public_dicom.py


Scraped from the following page:
http://dicom.nema.org/medical/dicom/current/output/chtml/part15/chapter_E.html

scrape date: 2024-09-19
"""

from idiscore.dicom import ActionCodes
from idiscore.identifiers import PrivateTags, RepeatingGroup, SingleTag
from idiscore.nema_parsing import RawNemaRuleSet

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
        (SingleTag("001811bb"), ActionCodes.DUMMY),  # AcquisitionFieldOfViewLabel
        (SingleTag("00189424"), ActionCodes.REMOVE),  # AcquisitionProtocolDescription
        (SingleTag("00080032"), ActionCodes.REMOVE_OR_EMPTY),  # AcquisitionTime
        (SingleTag("00080017"), ActionCodes.UID),  # AcquisitionUID
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
        (SingleTag("006a0006"), ActionCodes.REMOVE),  # AnnotationGroupDescription
        (SingleTag("006a0005"), ActionCodes.DUMMY),  # AnnotationGroupLabel
        (SingleTag("006a0003"), ActionCodes.DUMMY),  # AnnotationGroupUID
        (SingleTag("00440004"), ActionCodes.REMOVE),  # ApprovalStatusDateTime
        (SingleTag("40000010"), ActionCodes.REMOVE),  # Arbitrary
        (SingleTag("00440104"), ActionCodes.DUMMY),  # AssertionDateTime
        (SingleTag("00440105"), ActionCodes.REMOVE),  # AssertionExpirationDateTime
        (SingleTag("04000562"), ActionCodes.DUMMY),  # AttributeModificationDateTime
        (SingleTag("0040a078"), ActionCodes.REMOVE),  # AuthorObserverSequence
        (SingleTag("22000005"), ActionCodes.REMOVE_OR_EMPTY),  # BarcodeValue
        (SingleTag("300a00c3"), ActionCodes.REMOVE),  # BeamDescription
        (SingleTag("300c0127"), ActionCodes.DUMMY),  # BeamHoldTransitionDateTime
        (SingleTag("300a00dd"), ActionCodes.REMOVE),  # BolusDescription
        (SingleTag("00101081"), ActionCodes.REMOVE),  # BranchOfService
        (SingleTag("0014407e"), ActionCodes.REMOVE),  # CalibrationDate
        (SingleTag("00181203"), ActionCodes.EMPTY),  # CalibrationDateTime
        (SingleTag("0014407c"), ActionCodes.REMOVE),  # CalibrationTime
        (SingleTag("0016004d"), ActionCodes.REMOVE),  # CameraOwnerName
        (SingleTag("00181007"), ActionCodes.REMOVE),  # CassetteID
        (SingleTag("04000115"), ActionCodes.DUMMY),  # CertificateOfSigner
        (SingleTag("04000310"), ActionCodes.REMOVE),  # CertifiedTimestamp
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
        (SingleTag("00400310"), ActionCodes.REMOVE),  # CommentsOnRadiationDose
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
        (SingleTag("00700084"), ActionCodes.EMPTY_OR_DUMMY),  # ContentCreatorName
        (SingleTag("00080023"), ActionCodes.EMPTY_OR_DUMMY),  # ContentDate
        (SingleTag("0040a730"), ActionCodes.DUMMY),  # ContentSequence
        (SingleTag("00080033"), ActionCodes.EMPTY_OR_DUMMY),  # ContentTime
        (SingleTag("00080107"), ActionCodes.DUMMY),  # ContextGroupLocalVersion
        (SingleTag("00080106"), ActionCodes.DUMMY),  # ContextGroupVersion
        (SingleTag("00180010"), ActionCodes.EMPTY_OR_DUMMY),  # ContrastBolusAgent
        (SingleTag("00181042"), ActionCodes.REMOVE),  # ContrastBolusStartTime
        (SingleTag("00181043"), ActionCodes.REMOVE),  # ContrastBolusStopTime
        (SingleTag("0018a002"), ActionCodes.REMOVE),  # ContributionDateTime
        (SingleTag("0018a003"), ActionCodes.REMOVE),  # ContributionDescription
        (SingleTag("00102150"), ActionCodes.REMOVE),  # CountryOfResidence
        (SingleTag("21000040"), ActionCodes.REMOVE),  # CreationDate
        (SingleTag("21000050"), ActionCodes.REMOVE),  # CreationTime
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
        (SingleTag("0040a121"), ActionCodes.DUMMY),  # Date
        (
            SingleTag("0040a110"),
            ActionCodes.REMOVE,
        ),  # DateOfDocumentOrVerbalTransactionTrial
        (SingleTag("00181205"), ActionCodes.REMOVE),  # Unknown
        (SingleTag("00181200"), ActionCodes.REMOVE),  # DateOfLastCalibration
        (
            SingleTag("0018700c"),
            ActionCodes.REMOVE_OR_DUMMY,
        ),  # DateOfLastDetectorCalibration
        (SingleTag("00181204"), ActionCodes.REMOVE),  # Unknown
        (SingleTag("00181012"), ActionCodes.REMOVE),  # DateOfSecondaryCapture
        (SingleTag("0040a120"), ActionCodes.DUMMY),  # DateTime
        (SingleTag("00181202"), ActionCodes.REMOVE),  # DateTimeOfLastCalibration
        (SingleTag("00189701"), ActionCodes.DUMMY),  # DecayCorrectionDateTime
        (SingleTag("0018937f"), ActionCodes.REMOVE),  # DecompositionDescription
        (SingleTag("00082111"), ActionCodes.REMOVE),  # DerivationDescription
        (SingleTag("21000140"), ActionCodes.DUMMY),  # DestinationAE
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
        (SingleTag("04000105"), ActionCodes.DUMMY),  # DigitalSignatureDateTime
        (SingleTag("fffafffa"), ActionCodes.REMOVE),  # DigitalSignaturesSequence
        (SingleTag("04000100"), ActionCodes.UID),  # DigitalSignatureUID
        (SingleTag("00209164"), ActionCodes.UID),  # DimensionOrganizationUID
        (SingleTag("00380030"), ActionCodes.REMOVE),  # DischargeDate
        (SingleTag("00380040"), ActionCodes.REMOVE),  # DischargeDiagnosisDescription
        (SingleTag("00380032"), ActionCodes.REMOVE),  # DischargeTime
        (SingleTag("300a079a"), ActionCodes.REMOVE),  # DisplacementReferenceLabel
        (SingleTag("4008011a"), ActionCodes.REMOVE),  # DistributionAddress
        (SingleTag("40080119"), ActionCodes.REMOVE),  # DistributionName
        (SingleTag("300a0016"), ActionCodes.REMOVE),  # DoseReferenceDescription
        (SingleTag("300a0013"), ActionCodes.UID),  # DoseReferenceUID
        (SingleTag("3010006e"), ActionCodes.UID),  # DosimetricObjectiveUID
        (SingleTag("00686226"), ActionCodes.DUMMY),  # EffectiveDateTime
        (SingleTag("00420011"), ActionCodes.DUMMY),  # EncapsulatedDocument
        (SingleTag("00189517"), ActionCodes.REMOVE_OR_DUMMY),  # EndAcquisitionDateTime
        (SingleTag("30100037"), ActionCodes.REMOVE),  # EntityDescription
        (SingleTag("30100035"), ActionCodes.DUMMY),  # EntityLabel
        (SingleTag("30100038"), ActionCodes.DUMMY),  # EntityLongLabel
        (SingleTag("30100036"), ActionCodes.REMOVE),  # EntityName
        (
            SingleTag("300a0676"),
            ActionCodes.REMOVE,
        ),  # EquipmentFrameOfReferenceDescription
        (
            SingleTag("00120087"),
            ActionCodes.REMOVE,
        ),  # EthicsCommitteeApprovalEffectivenessEndDate
        (
            SingleTag("00120086"),
            ActionCodes.REMOVE,
        ),  # EthicsCommitteeApprovalEffectivenessStartDate
        (SingleTag("00102160"), ActionCodes.REMOVE),  # EthnicGroup
        (SingleTag("00102161"), ActionCodes.REMOVE),  # Unknown
        (SingleTag("00189804"), ActionCodes.DUMMY),  # ExclusionStartDateTime
        (SingleTag("00404011"), ActionCodes.REMOVE),  # ExpectedCompletionDateTime
        (SingleTag("00080058"), ActionCodes.UID),  # FailedSOPInstanceUIDList
        (SingleTag("0070031a"), ActionCodes.UID),  # FiducialUID
        (
            SingleTag("00402017"),
            ActionCodes.EMPTY,
        ),  # FillerOrderNumberImagingServiceRequest
        (SingleTag("003a032b"), ActionCodes.REMOVE),  # FilterLookupTableDescription
        (SingleTag("0040a023"), ActionCodes.REMOVE),  # FindingsGroupRecordingDateTrial
        (SingleTag("0040a024"), ActionCodes.REMOVE),  # FindingsGroupRecordingTimeTrial
        (SingleTag("30080054"), ActionCodes.REMOVE_OR_DUMMY),  # FirstTreatmentDate
        (SingleTag("300a0196"), ActionCodes.REMOVE),  # FixationDeviceDescription
        (SingleTag("00340002"), ActionCodes.DUMMY),  # FlowIdentifier
        (SingleTag("00340001"), ActionCodes.DUMMY),  # FlowIdentifierSequence
        (SingleTag("3010007f"), ActionCodes.EMPTY),  # FractionationNotes
        (SingleTag("300a0072"), ActionCodes.REMOVE),  # FractionGroupDescription
        (SingleTag("00189074"), ActionCodes.DUMMY),  # FrameAcquisitionDateTime
        (SingleTag("00209158"), ActionCodes.REMOVE),  # FrameComments
        (SingleTag("00200052"), ActionCodes.UID),  # FrameOfReferenceUID
        (SingleTag("00340007"), ActionCodes.DUMMY),  # FrameOriginTimestamp
        (SingleTag("00189151"), ActionCodes.DUMMY),  # FrameReferenceDateTime
        (SingleTag("00189623"), ActionCodes.DUMMY),  # FunctionalSyncPulse
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
        (SingleTag("0072000a"), ActionCodes.DUMMY),  # HangingProtocolCreationDateTime
        (SingleTag("0040e004"), ActionCodes.REMOVE),  # HL7DocumentEffectiveTime
        (SingleTag("00404037"), ActionCodes.REMOVE),  # HumanPerformerName
        (SingleTag("00404036"), ActionCodes.REMOVE),  # HumanPerformerOrganization
        (SingleTag("00880200"), ActionCodes.REMOVE),  # IconImageSequence
        (SingleTag("00084000"), ActionCodes.REMOVE),  # IdentifyingComments
        (SingleTag("00204000"), ActionCodes.REMOVE),  # ImageComments
        (SingleTag("00284000"), ActionCodes.REMOVE),  # ImagePresentationComments
        (SingleTag("00402400"), ActionCodes.REMOVE),  # ImagingServiceRequestComments
        (SingleTag("003a0314"), ActionCodes.DUMMY),  # ImpedanceMeasurementDateTime
        (SingleTag("40080300"), ActionCodes.REMOVE),  # Impressions
        (SingleTag("00686270"), ActionCodes.DUMMY),  # InformationIssueDateTime
        (SingleTag("00080015"), ActionCodes.REMOVE),  # InstanceCoercionDateTime
        (SingleTag("00080012"), ActionCodes.REMOVE_OR_DUMMY),  # InstanceCreationDate
        (
            SingleTag("00080013"),
            ActionCodes.REMOVE_OR_EMPTY_OR_DUMMY,
        ),  # InstanceCreationTime
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
        (
            SingleTag("00189919"),
            ActionCodes.EMPTY_OR_DUMMY,
        ),  # InstructionPerformedDateTime
        (SingleTag("00101050"), ActionCodes.REMOVE),  # InsurancePlanIdentification
        (SingleTag("30100085"), ActionCodes.REMOVE),  # IntendedFractionStartTime
        (SingleTag("3010004d"), ActionCodes.REMOVE_OR_DUMMY),  # IntendedPhaseEndDate
        (SingleTag("3010004c"), ActionCodes.REMOVE_OR_DUMMY),  # IntendedPhaseStartDate
        (
            SingleTag("00401011"),
            ActionCodes.REMOVE,
        ),  # IntendedRecipientsOfResultsIdentificationSequence
        (SingleTag("300a0741"), ActionCodes.DUMMY),  # InterlockDateTime
        (SingleTag("300a0742"), ActionCodes.DUMMY),  # InterlockDescription
        (SingleTag("300a0783"), ActionCodes.DUMMY),  # InterlockOriginDescription
        (SingleTag("40080112"), ActionCodes.REMOVE),  # InterpretationApprovalDate
        (SingleTag("40080113"), ActionCodes.REMOVE),  # InterpretationApprovalTime
        (SingleTag("40080111"), ActionCodes.REMOVE),  # InterpretationApproverSequence
        (SingleTag("4008010c"), ActionCodes.REMOVE),  # InterpretationAuthor
        (
            SingleTag("40080115"),
            ActionCodes.REMOVE,
        ),  # InterpretationDiagnosisDescription
        (SingleTag("40080200"), ActionCodes.REMOVE),  # InterpretationID
        (SingleTag("40080202"), ActionCodes.REMOVE),  # InterpretationIDIssuer
        (SingleTag("40080100"), ActionCodes.REMOVE),  # InterpretationRecordedDate
        (SingleTag("40080101"), ActionCodes.REMOVE),  # InterpretationRecordedTime
        (SingleTag("40080102"), ActionCodes.REMOVE),  # InterpretationRecorder
        (SingleTag("4008010b"), ActionCodes.REMOVE),  # InterpretationText
        (SingleTag("4008010a"), ActionCodes.REMOVE),  # InterpretationTranscriber
        (SingleTag("40080108"), ActionCodes.REMOVE),  # InterpretationTranscriptionDate
        (SingleTag("40080109"), ActionCodes.REMOVE),  # InterpretationTranscriptionTime
        (SingleTag("00180035"), ActionCodes.REMOVE),  # InterventionDrugStartTime
        (SingleTag("00180027"), ActionCodes.REMOVE),  # InterventionDrugStopTime
        (SingleTag("00083010"), ActionCodes.UID),  # IrradiationEventUID
        (SingleTag("00402004"), ActionCodes.REMOVE),  # IssueDateOfImagingServiceRequest
        (SingleTag("00380011"), ActionCodes.REMOVE),  # IssuerOfAdmissionID
        (SingleTag("00380014"), ActionCodes.REMOVE),  # IssuerOfAdmissionIDSequence
        (SingleTag("00120022"), ActionCodes.REMOVE),  # Unknown
        (SingleTag("00120073"), ActionCodes.REMOVE),  # Unknown
        (SingleTag("00120032"), ActionCodes.REMOVE),  # Unknown
        (SingleTag("00120041"), ActionCodes.REMOVE),  # Unknown
        (SingleTag("00120043"), ActionCodes.REMOVE),  # Unknown
        (SingleTag("00120055"), ActionCodes.REMOVE),  # Unknown
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
        (SingleTag("00402005"), ActionCodes.REMOVE),  # IssueTimeOfImagingServiceRequest
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
        (SingleTag("00203403"), ActionCodes.REMOVE),  # ModifiedImageDate
        (SingleTag("00203406"), ActionCodes.REMOVE),  # ModifiedImageDescription
        (SingleTag("00203405"), ActionCodes.REMOVE),  # ModifiedImageTime
        (SingleTag("00203401"), ActionCodes.REMOVE),  # ModifyingDeviceID
        (SingleTag("04000563"), ActionCodes.DUMMY),  # ModifyingSystem
        (SingleTag("30080056"), ActionCodes.REMOVE_OR_DUMMY),  # MostRecentTreatmentDate
        (
            SingleTag("0018937b"),
            ActionCodes.REMOVE,
        ),  # MultienergyAcquisitionDescription
        (SingleTag("003a0310"), ActionCodes.UID),  # MultiplexGroupUID
        (SingleTag("00081060"), ActionCodes.REMOVE),  # NameOfPhysiciansReadingStudy
        (
            SingleTag("00401010"),
            ActionCodes.REMOVE,
        ),  # NamesOfIntendedRecipientsOfResults
        (SingleTag("00081000"), ActionCodes.REMOVE),  # NetworkID
        (SingleTag("04000552"), ActionCodes.REMOVE),  # NonconformingDataElementValue
        (
            SingleTag("04000551"),
            ActionCodes.REMOVE,
        ),  # NonconformingModifiedAttributesSequence
        (SingleTag("0040a192"), ActionCodes.REMOVE),  # ObservationDateTrial
        (SingleTag("0040a032"), ActionCodes.REMOVE_OR_DUMMY),  # ObservationDateTime
        (SingleTag("0040a033"), ActionCodes.REMOVE),  # ObservationStartDateTime
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
        (SingleTag("21000070"), ActionCodes.REMOVE),  # Originator
        (SingleTag("00120023"), ActionCodes.REMOVE),  # Unknown
        (SingleTag("00101000"), ActionCodes.REMOVE),  # OtherPatientIDs
        (SingleTag("00101002"), ActionCodes.REMOVE),  # OtherPatientIDsSequence
        (SingleTag("00101001"), ActionCodes.REMOVE),  # OtherPatientNames
        (RepeatingGroup("60xx4000"), ActionCodes.REMOVE),  # OverlayComments
        (RepeatingGroup("60xx3000"), ActionCodes.REMOVE),  # OverlayData
        (SingleTag("00080024"), ActionCodes.REMOVE),  # OverlayDate
        (SingleTag("00080034"), ActionCodes.REMOVE),  # OverlayTime
        (SingleTag("300a0760"), ActionCodes.DUMMY),  # OverrideDateTime
        (SingleTag("00281199"), ActionCodes.UID),  # PaletteColorLookupTableUID
        (SingleTag("0040a07a"), ActionCodes.REMOVE),  # ParticipantSequence
        (SingleTag("0040a082"), ActionCodes.EMPTY),  # ParticipationDateTime
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
        (SingleTag("00100020"), ActionCodes.EMPTY_OR_DUMMY),  # PatientID
        (SingleTag("300a0794"), ActionCodes.REMOVE),  # PatientSetupPhotoDescription
        (SingleTag("300a0650"), ActionCodes.UID),  # PatientSetupUID
        (SingleTag("00380500"), ActionCodes.REMOVE),  # PatientState
        (SingleTag("00401004"), ActionCodes.REMOVE),  # PatientTransportArrangements
        (
            SingleTag("300a0792"),
            ActionCodes.REMOVE,
        ),  # PatientTreatmentPreparationMethodDescription
        (
            SingleTag("300a078e"),
            ActionCodes.REMOVE,
        ),  # PatientTreatmentPreparationProcedureParameterDescription
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
        (
            SingleTag("30020123"),
            ActionCodes.REMOVE,
        ),  # PositionAcquisitionTemplateDescription
        (SingleTag("30020121"), ActionCodes.REMOVE),  # PositionAcquisitionTemplateName
        (SingleTag("001021c0"), ActionCodes.REMOVE),  # PregnancyStatus
        (SingleTag("00400012"), ActionCodes.REMOVE),  # PreMedication
        (SingleTag("300a000e"), ActionCodes.REMOVE),  # PrescriptionDescription
        (SingleTag("3010007b"), ActionCodes.EMPTY),  # PrescriptionNotes
        (SingleTag("30100081"), ActionCodes.EMPTY),  # PrescriptionNotesSequence
        (SingleTag("00700082"), ActionCodes.REMOVE),  # PresentationCreationDate
        (SingleTag("00700083"), ActionCodes.REMOVE),  # PresentationCreationTime
        (SingleTag("00701101"), ActionCodes.UID),  # PresentationDisplayCollectionUID
        (SingleTag("00701102"), ActionCodes.UID),  # PresentationSequenceCollectionUID
        (SingleTag("30100061"), ActionCodes.REMOVE),  # PriorTreatmentDoseDescription
        (PrivateTags(), ActionCodes.REMOVE),  # Private Attributes
        (
            SingleTag("00404052"),
            ActionCodes.REMOVE,
        ),  # ProcedureStepCancellationDateTime
        (SingleTag("0044000b"), ActionCodes.REMOVE),  # ProductExpirationDateTime
        (SingleTag("00181030"), ActionCodes.REMOVE_OR_DUMMY),  # ProtocolName
        (SingleTag("00081088"), ActionCodes.REMOVE),  # PyramidDescription
        (SingleTag("00200027"), ActionCodes.REMOVE),  # PyramidLabel
        (SingleTag("00080019"), ActionCodes.UID),  # PyramidUID
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
        (SingleTag("00181078"), ActionCodes.REMOVE),  # RadiopharmaceuticalStartDateTime
        (SingleTag("00181072"), ActionCodes.REMOVE),  # RadiopharmaceuticalStartTime
        (SingleTag("00181079"), ActionCodes.REMOVE),  # RadiopharmaceuticalStopDateTime
        (SingleTag("00181073"), ActionCodes.REMOVE),  # RadiopharmaceuticalStopTime
        (SingleTag("300c0113"), ActionCodes.REMOVE),  # ReasonForOmissionDescription
        (
            SingleTag("0040100a"),
            ActionCodes.REMOVE,
        ),  # ReasonForRequestedProcedureCodeSequence
        (SingleTag("00321030"), ActionCodes.REMOVE),  # ReasonForStudy
        (SingleTag("3010005c"), ActionCodes.EMPTY),  # ReasonForSuperseding
        (SingleTag("04000565"), ActionCodes.DUMMY),  # ReasonForTheAttributeModification
        (
            SingleTag("00402001"),
            ActionCodes.REMOVE,
        ),  # ReasonForTheImagingServiceRequest
        (SingleTag("00401002"), ActionCodes.REMOVE),  # ReasonForTheRequestedProcedure
        (SingleTag("00321066"), ActionCodes.REMOVE),  # ReasonForVisit
        (SingleTag("00321067"), ActionCodes.REMOVE),  # ReasonForVisitCodeSequence
        (SingleTag("00741234"), ActionCodes.REMOVE),  # ReceivingAE
        (SingleTag("300a073a"), ActionCodes.DUMMY),  # RecordedRTControlPointDateTime
        (SingleTag("3010000b"), ActionCodes.UID),  # ReferencedConceptualVolumeUID
        (SingleTag("0040a13a"), ActionCodes.DUMMY),  # ReferencedDateTime
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
        (SingleTag("300a0785"), ActionCodes.UID),  # ReferencedTreatmentPositionGroupUID
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
        (SingleTag("00189937"), ActionCodes.REMOVE),  # RequestedSeriesDescription
        (SingleTag("00001001"), ActionCodes.UID),  # RequestedSOPInstanceUID
        (SingleTag("00741236"), ActionCodes.REMOVE),  # RequestingAE
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
        (SingleTag("40080040"), ActionCodes.REMOVE),  # ResultsID
        (SingleTag("40080042"), ActionCodes.REMOVE),  # ResultsIDIssuer
        (SingleTag("00080054"), ActionCodes.REMOVE),  # RetrieveAETitle
        (SingleTag("300e0004"), ActionCodes.EMPTY),  # ReviewDate
        (SingleTag("300e0008"), ActionCodes.REMOVE_OR_EMPTY),  # ReviewerName
        (SingleTag("300e0005"), ActionCodes.EMPTY),  # ReviewTime
        (SingleTag("3006004d"), ActionCodes.REMOVE),  # Unknown
        (SingleTag("3006002d"), ActionCodes.REMOVE),  # Unknown
        (SingleTag("30060028"), ActionCodes.REMOVE),  # ROIDescription
        (SingleTag("30060038"), ActionCodes.REMOVE),  # ROIGenerationDescription
        (SingleTag("300600a6"), ActionCodes.EMPTY),  # ROIInterpreter
        (SingleTag("3006004e"), ActionCodes.REMOVE),  # Unknown
        (SingleTag("30060026"), ActionCodes.EMPTY),  # ROIName
        (SingleTag("3006002e"), ActionCodes.REMOVE),  # Unknown
        (SingleTag("30060088"), ActionCodes.REMOVE),  # ROIObservationDescription
        (SingleTag("30060085"), ActionCodes.REMOVE),  # ROIObservationLabel
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
        (SingleTag("30080162"), ActionCodes.DUMMY),  # SafePositionExitDate
        (SingleTag("30080164"), ActionCodes.DUMMY),  # SafePositionExitTime
        (SingleTag("30080166"), ActionCodes.DUMMY),  # SafePositionReturnDate
        (SingleTag("30080168"), ActionCodes.DUMMY),  # SafePositionReturnTime
        (SingleTag("0038001a"), ActionCodes.REMOVE),  # ScheduledAdmissionDate
        (SingleTag("0038001b"), ActionCodes.REMOVE),  # ScheduledAdmissionTime
        (SingleTag("0038001c"), ActionCodes.REMOVE),  # ScheduledDischargeDate
        (SingleTag("0038001d"), ActionCodes.REMOVE),  # ScheduledDischargeTime
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
        (SingleTag("00400009"), ActionCodes.REMOVE),  # ScheduledProcedureStepID
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
        (SingleTag("00321000"), ActionCodes.REMOVE),  # ScheduledStudyStartDate
        (SingleTag("00321001"), ActionCodes.REMOVE),  # ScheduledStudyStartTime
        (SingleTag("00321010"), ActionCodes.REMOVE),  # ScheduledStudyStopDate
        (SingleTag("00321011"), ActionCodes.REMOVE),  # ScheduledStudyStopTime
        (SingleTag("0072005e"), ActionCodes.DUMMY),  # SelectorAEValue
        (SingleTag("0072005f"), ActionCodes.DUMMY),  # SelectorASValue
        (SingleTag("00720061"), ActionCodes.DUMMY),  # SelectorDAValue
        (SingleTag("00720063"), ActionCodes.DUMMY),  # SelectorDTValue
        (SingleTag("00720066"), ActionCodes.DUMMY),  # SelectorLOValue
        (SingleTag("00720068"), ActionCodes.DUMMY),  # SelectorLTValue
        (SingleTag("00720065"), ActionCodes.DUMMY),  # SelectorOBValue
        (SingleTag("0072006a"), ActionCodes.DUMMY),  # SelectorPNValue
        (SingleTag("0072006c"), ActionCodes.DUMMY),  # SelectorSHValue
        (SingleTag("0072006e"), ActionCodes.DUMMY),  # SelectorSTValue
        (SingleTag("0072006b"), ActionCodes.DUMMY),  # SelectorTMValue
        (SingleTag("0072006d"), ActionCodes.DUMMY),  # SelectorUNValue
        (SingleTag("00720071"), ActionCodes.DUMMY),  # SelectorURValue
        (SingleTag("00720070"), ActionCodes.DUMMY),  # SelectorUTValue
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
        (SingleTag("01000420"), ActionCodes.REMOVE),  # SOPAuthorizationDateTime
        (SingleTag("00080018"), ActionCodes.UID),  # SOPInstanceUID
        (SingleTag("30100015"), ActionCodes.UID),  # SourceConceptualVolumeUID
        (SingleTag("0018936a"), ActionCodes.DUMMY),  # SourceEndDateTime
        (SingleTag("00640003"), ActionCodes.UID),  # SourceFrameOfReferenceUID
        (SingleTag("00340005"), ActionCodes.DUMMY),  # SourceIdentifier
        (
            SingleTag("00082112"),
            ActionCodes.REMOVE_OR_EMPTY_OR_UID,
        ),  # SourceImageSequence
        (SingleTag("300a0216"), ActionCodes.REMOVE),  # SourceManufacturer
        (SingleTag("04000564"), ActionCodes.EMPTY),  # SourceOfPreviousValues
        (SingleTag("30080105"), ActionCodes.REMOVE_OR_EMPTY),  # SourceSerialNumber
        (SingleTag("00189369"), ActionCodes.DUMMY),  # SourceStartDateTime
        (SingleTag("300a022c"), ActionCodes.DUMMY),  # SourceStrengthReferenceDate
        (SingleTag("300a022e"), ActionCodes.DUMMY),  # SourceStrengthReferenceTime
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
        (SingleTag("00080055"), ActionCodes.REMOVE),  # StationAETitle
        (SingleTag("00081010"), ActionCodes.REMOVE_OR_EMPTY_OR_DUMMY),  # StationName
        (SingleTag("00880140"), ActionCodes.UID),  # StorageMediaFileSetUID
        (SingleTag("30060008"), ActionCodes.EMPTY),  # StructureSetDate
        (SingleTag("30060006"), ActionCodes.REMOVE),  # StructureSetDescription
        (SingleTag("30060002"), ActionCodes.DUMMY),  # StructureSetLabel
        (SingleTag("30060004"), ActionCodes.REMOVE),  # StructureSetName
        (SingleTag("30060009"), ActionCodes.EMPTY),  # StructureSetTime
        (SingleTag("00321040"), ActionCodes.REMOVE),  # StudyArrivalDate
        (SingleTag("00321041"), ActionCodes.REMOVE),  # StudyArrivalTime
        (SingleTag("00324000"), ActionCodes.REMOVE),  # StudyComments
        (SingleTag("00321050"), ActionCodes.REMOVE),  # StudyCompletionDate
        (SingleTag("00321051"), ActionCodes.REMOVE),  # StudyCompletionTime
        (SingleTag("00080020"), ActionCodes.EMPTY),  # StudyDate
        (SingleTag("00081030"), ActionCodes.REMOVE),  # StudyDescription
        (SingleTag("00200010"), ActionCodes.EMPTY),  # StudyID
        (SingleTag("00320012"), ActionCodes.REMOVE),  # StudyIDIssuer
        (SingleTag("0020000d"), ActionCodes.UID),  # StudyInstanceUID
        (SingleTag("00320034"), ActionCodes.REMOVE),  # StudyReadDate
        (SingleTag("00320035"), ActionCodes.REMOVE),  # StudyReadTime
        (SingleTag("00080030"), ActionCodes.EMPTY),  # StudyTime
        (SingleTag("00320032"), ActionCodes.REMOVE),  # StudyVerifiedDate
        (SingleTag("00320033"), ActionCodes.REMOVE),  # StudyVerifiedTime
        (SingleTag("00440010"), ActionCodes.REMOVE),  # SubstanceAdministrationDateTime
        (SingleTag("00200200"), ActionCodes.UID),  # SynchronizationFrameOfReferenceUID
        (SingleTag("300a0054"), ActionCodes.UID),  # Unknown
        (SingleTag("00182042"), ActionCodes.UID),  # TargetUID
        (SingleTag("0040a354"), ActionCodes.REMOVE),  # TelephoneNumberTrial
        (SingleTag("0040db0d"), ActionCodes.UID),  # TemplateExtensionCreatorUID
        (SingleTag("0040db0c"), ActionCodes.UID),  # TemplateExtensionOrganizationUID
        (SingleTag("0040db07"), ActionCodes.REMOVE),  # TemplateLocalVersion
        (SingleTag("0040db06"), ActionCodes.REMOVE),  # TemplateVersion
        (SingleTag("40004000"), ActionCodes.REMOVE),  # TextComments
        (SingleTag("20300020"), ActionCodes.REMOVE),  # TextString
        (SingleTag("0040a122"), ActionCodes.DUMMY),  # Time
        (
            SingleTag("0040a112"),
            ActionCodes.REMOVE,
        ),  # TimeOfDocumentCreationOrVerbalTransactionTrial
        (SingleTag("00181201"), ActionCodes.REMOVE),  # TimeOfLastCalibration
        (
            SingleTag("0018700e"),
            ActionCodes.REMOVE_OR_DUMMY,
        ),  # TimeOfLastDetectorCalibration
        (SingleTag("00181014"), ActionCodes.REMOVE),  # TimeOfSecondaryCapture
        (SingleTag("00080201"), ActionCodes.REMOVE),  # TimezoneOffsetFromUTC
        (SingleTag("00880910"), ActionCodes.REMOVE),  # TopicAuthor
        (SingleTag("00880912"), ActionCodes.REMOVE),  # TopicKeywords
        (SingleTag("00880906"), ActionCodes.REMOVE),  # TopicSubject
        (SingleTag("00880904"), ActionCodes.REMOVE),  # TopicTitle
        (SingleTag("00620021"), ActionCodes.UID),  # TrackingUID
        (SingleTag("00081195"), ActionCodes.UID),  # TransactionUID
        (SingleTag("00185011"), ActionCodes.REMOVE),  # TransducerIdentificationSequence
        (SingleTag("30080024"), ActionCodes.DUMMY),  # TreatmentControlPointDate
        (SingleTag("30080025"), ActionCodes.DUMMY),  # TreatmentControlPointTime
        (SingleTag("30080250"), ActionCodes.REMOVE_OR_DUMMY),  # TreatmentDate
        (SingleTag("300a00b2"), ActionCodes.REMOVE_OR_EMPTY),  # TreatmentMachineName
        (SingleTag("300a0608"), ActionCodes.DUMMY),  # TreatmentPositionGroupLabel
        (SingleTag("300a0609"), ActionCodes.UID),  # TreatmentPositionGroupUID
        (SingleTag("300a0700"), ActionCodes.UID),  # TreatmentSessionUID
        (SingleTag("30100077"), ActionCodes.REMOVE_OR_DUMMY),  # TreatmentSite
        (SingleTag("300a000b"), ActionCodes.REMOVE),  # TreatmentSites
        (SingleTag("3010007a"), ActionCodes.EMPTY),  # TreatmentTechniqueNotes
        (SingleTag("30080251"), ActionCodes.REMOVE_OR_DUMMY),  # TreatmentTime
        (
            SingleTag("300a0736"),
            ActionCodes.DUMMY,
        ),  # TreatmentToleranceViolationDateTime
        (
            SingleTag("300a0734"),
            ActionCodes.DUMMY,
        ),  # TreatmentToleranceViolationDescription
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
        (SingleTag("0040a030"), ActionCodes.DUMMY),  # VerificationDateTime
        (
            SingleTag("0040a088"),
            ActionCodes.EMPTY,
        ),  # VerifyingObserverIdentificationCodeSequence
        (SingleTag("0040a075"), ActionCodes.DUMMY),  # VerifyingObserverName
        (SingleTag("0040a073"), ActionCodes.DUMMY),  # VerifyingObserverSequence
        (SingleTag("0040a027"), ActionCodes.DUMMY),  # VerifyingOrganization
        (SingleTag("00384000"), ActionCodes.REMOVE),  # VisitComments
        (SingleTag("003a0329"), ActionCodes.REMOVE),  # WaveformFilterDescription
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
        (SingleTag("00080017"), ActionCodes.KEEP),  # AcquisitionUID
        (SingleTag("00001000"), ActionCodes.KEEP),  # AffectedSOPInstanceUID
        (SingleTag("006a0003"), ActionCodes.KEEP),  # AnnotationGroupUID
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
        (SingleTag("003a0310"), ActionCodes.KEEP),  # MultiplexGroupUID
        (SingleTag("0040a402"), ActionCodes.KEEP),  # ObservationSubjectUIDTrial
        (SingleTag("0040a171"), ActionCodes.KEEP),  # ObservationUID
        (SingleTag("00281199"), ActionCodes.KEEP),  # PaletteColorLookupTableUID
        (SingleTag("300a0650"), ActionCodes.KEEP),  # PatientSetupUID
        (SingleTag("00701101"), ActionCodes.KEEP),  # PresentationDisplayCollectionUID
        (SingleTag("00701102"), ActionCodes.KEEP),  # PresentationSequenceCollectionUID
        (SingleTag("00080019"), ActionCodes.KEEP),  # PyramidUID
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
        (SingleTag("00081120"), ActionCodes.KEEP),  # ReferencedPatientSequence
        (
            SingleTag("00081111"),
            ActionCodes.KEEP,
        ),  # ReferencedPerformedProcedureStepSequence
        (SingleTag("00081155"), ActionCodes.KEEP),  # ReferencedSOPInstanceUID
        (SingleTag("00041511"), ActionCodes.KEEP),  # ReferencedSOPInstanceUIDInFile
        (SingleTag("00081110"), ActionCodes.KEEP),  # ReferencedStudySequence
        (
            SingleTag("300a0785"),
            ActionCodes.KEEP,
        ),  # ReferencedTreatmentPositionGroupUID
        (SingleTag("300600c2"), ActionCodes.KEEP),  # RelatedFrameOfReferenceUID
        (SingleTag("00001001"), ActionCodes.KEEP),  # RequestedSOPInstanceUID
        (SingleTag("3010003b"), ActionCodes.KEEP),  # RTTreatmentPhaseUID
        (SingleTag("0020000e"), ActionCodes.KEEP),  # SeriesInstanceUID
        (SingleTag("00080018"), ActionCodes.KEEP),  # SOPInstanceUID
        (SingleTag("30100015"), ActionCodes.KEEP),  # SourceConceptualVolumeUID
        (SingleTag("00640003"), ActionCodes.KEEP),  # SourceFrameOfReferenceUID
        (SingleTag("00082112"), ActionCodes.KEEP),  # SourceImageSequence
        (SingleTag("00400554"), ActionCodes.KEEP),  # SpecimenUID
        (SingleTag("00880140"), ActionCodes.KEEP),  # StorageMediaFileSetUID
        (SingleTag("0020000d"), ActionCodes.KEEP),  # StudyInstanceUID
        (SingleTag("00200200"), ActionCodes.KEEP),  # SynchronizationFrameOfReferenceUID
        (SingleTag("300a0054"), ActionCodes.KEEP),  # Unknown
        (SingleTag("00182042"), ActionCodes.KEEP),  # TargetUID
        (SingleTag("0040db0d"), ActionCodes.KEEP),  # TemplateExtensionCreatorUID
        (SingleTag("0040db0c"), ActionCodes.KEEP),  # TemplateExtensionOrganizationUID
        (SingleTag("00620021"), ActionCodes.KEEP),  # TrackingUID
        (SingleTag("00081195"), ActionCodes.KEEP),  # TransactionUID
        (SingleTag("300a0609"), ActionCodes.KEEP),  # TreatmentPositionGroupUID
        (SingleTag("300a0700"), ActionCodes.KEEP),  # TreatmentSessionUID
    ],
)

retain_device_id = RawNemaRuleSet(
    name="Retain Device Identity Option",
    code="113109",
    rules=[
        (SingleTag("300c0127"), ActionCodes.KEEP),  # BeamHoldTransitionDateTime
        (SingleTag("0014407e"), ActionCodes.KEEP),  # CalibrationDate
        (SingleTag("00181203"), ActionCodes.KEEP),  # CalibrationDateTime
        (SingleTag("0014407c"), ActionCodes.KEEP),  # CalibrationTime
        (SingleTag("00181007"), ActionCodes.KEEP),  # CassetteID
        (SingleTag("00181205"), ActionCodes.KEEP),  # Unknown
        (SingleTag("00181200"), ActionCodes.KEEP),  # DateOfLastCalibration
        (SingleTag("0018700c"), ActionCodes.KEEP),  # DateOfLastDetectorCalibration
        (SingleTag("00181204"), ActionCodes.KEEP),  # Unknown
        (SingleTag("00181202"), ActionCodes.KEEP),  # DateTimeOfLastCalibration
        (SingleTag("21000140"), ActionCodes.CLEAN),  # DestinationAE
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
        (SingleTag("00203401"), ActionCodes.KEEP),  # ModifyingDeviceID
        (SingleTag("04000563"), ActionCodes.KEEP),  # ModifyingSystem
        (SingleTag("00081000"), ActionCodes.CLEAN),  # NetworkID
        (SingleTag("21000070"), ActionCodes.CLEAN),  # Originator
        (SingleTag("00400241"), ActionCodes.CLEAN),  # PerformedStationAETitle
        (
            SingleTag("00404030"),
            ActionCodes.KEEP,
        ),  # PerformedStationGeographicLocationCodeSequence
        (SingleTag("00400242"), ActionCodes.KEEP),  # PerformedStationName
        (SingleTag("00404028"), ActionCodes.KEEP),  # PerformedStationNameCodeSequence
        (SingleTag("00181004"), ActionCodes.KEEP),  # PlateID
        (SingleTag("00741234"), ActionCodes.CLEAN),  # ReceivingAE
        (SingleTag("00741236"), ActionCodes.CLEAN),  # RequestingAE
        (SingleTag("00080054"), ActionCodes.CLEAN),  # RetrieveAETitle
        (SingleTag("00400011"), ActionCodes.KEEP),  # ScheduledProcedureStepLocation
        (SingleTag("00400001"), ActionCodes.CLEAN),  # ScheduledStationAETitle
        (
            SingleTag("00404027"),
            ActionCodes.KEEP,
        ),  # ScheduledStationGeographicLocationCodeSequence
        (SingleTag("00400010"), ActionCodes.KEEP),  # ScheduledStationName
        (SingleTag("00404025"), ActionCodes.KEEP),  # ScheduledStationNameCodeSequence
        (SingleTag("00321020"), ActionCodes.KEEP),  # ScheduledStudyLocation
        (SingleTag("00321021"), ActionCodes.CLEAN),  # ScheduledStudyLocationAETitle
        (SingleTag("0072005e"), ActionCodes.CLEAN),  # SelectorAEValue
        (SingleTag("300a0216"), ActionCodes.KEEP),  # SourceManufacturer
        (SingleTag("30080105"), ActionCodes.KEEP),  # SourceSerialNumber
        (SingleTag("00080055"), ActionCodes.CLEAN),  # StationAETitle
        (SingleTag("00081010"), ActionCodes.KEEP),  # StationName
        (SingleTag("00181201"), ActionCodes.KEEP),  # TimeOfLastCalibration
        (SingleTag("0018700e"), ActionCodes.KEEP),  # TimeOfLastDetectorCalibration
        (SingleTag("00185011"), ActionCodes.KEEP),  # TransducerIdentificationSequence
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
        (SingleTag("04000564"), ActionCodes.KEEP),  # SourceOfPreviousValues
    ],
)

retain_patient_characteristics = RawNemaRuleSet(
    name="Retain Patient Characteristics Option",
    code="113108",
    rules=[
        (SingleTag("00102110"), ActionCodes.CLEAN),  # Allergies
        (SingleTag("00102160"), ActionCodes.KEEP),  # EthnicGroup
        (SingleTag("00102161"), ActionCodes.KEEP),  # Unknown
        (SingleTag("00101010"), ActionCodes.KEEP),  # PatientAge
        (SingleTag("00100040"), ActionCodes.KEEP),  # PatientSex
        (SingleTag("00102203"), ActionCodes.KEEP),  # PatientSexNeutered
        (SingleTag("00101020"), ActionCodes.KEEP),  # PatientSize
        (SingleTag("00101030"), ActionCodes.KEEP),  # PatientWeight
        (SingleTag("00380500"), ActionCodes.CLEAN),  # PatientState
        (SingleTag("001021c0"), ActionCodes.KEEP),  # PregnancyStatus
        (SingleTag("00400012"), ActionCodes.CLEAN),  # PreMedication
        (SingleTag("0072005f"), ActionCodes.KEEP),  # SelectorASValue
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
        (SingleTag("00440004"), ActionCodes.KEEP),  # ApprovalStatusDateTime
        (SingleTag("00440104"), ActionCodes.KEEP),  # AssertionDateTime
        (SingleTag("00440105"), ActionCodes.KEEP),  # AssertionExpirationDateTime
        (SingleTag("04000562"), ActionCodes.KEEP),  # AttributeModificationDateTime
        (SingleTag("300c0127"), ActionCodes.KEEP),  # BeamHoldTransitionDateTime
        (SingleTag("0014407e"), ActionCodes.KEEP),  # CalibrationDate
        (SingleTag("00181203"), ActionCodes.KEEP),  # CalibrationDateTime
        (SingleTag("0014407c"), ActionCodes.KEEP),  # CalibrationTime
        (SingleTag("04000310"), ActionCodes.KEEP),  # CertifiedTimestamp
        (SingleTag("00080023"), ActionCodes.KEEP),  # ContentDate
        (SingleTag("00080033"), ActionCodes.KEEP),  # ContentTime
        (SingleTag("00080107"), ActionCodes.KEEP),  # ContextGroupLocalVersion
        (SingleTag("00080106"), ActionCodes.KEEP),  # ContextGroupVersion
        (SingleTag("00181042"), ActionCodes.KEEP),  # ContrastBolusStartTime
        (SingleTag("00181043"), ActionCodes.KEEP),  # ContrastBolusStopTime
        (SingleTag("0018a002"), ActionCodes.KEEP),  # ContributionDateTime
        (SingleTag("21000040"), ActionCodes.KEEP),  # CreationDate
        (SingleTag("21000050"), ActionCodes.KEEP),  # CreationTime
        (SingleTag("00080025"), ActionCodes.KEEP),  # CurveDate
        (SingleTag("00080035"), ActionCodes.KEEP),  # CurveTime
        (SingleTag("0040a121"), ActionCodes.KEEP),  # Date
        (
            SingleTag("0040a110"),
            ActionCodes.KEEP,
        ),  # DateOfDocumentOrVerbalTransactionTrial
        (SingleTag("00181205"), ActionCodes.KEEP),  # Unknown
        (SingleTag("00181200"), ActionCodes.KEEP),  # DateOfLastCalibration
        (SingleTag("0018700c"), ActionCodes.KEEP),  # DateOfLastDetectorCalibration
        (SingleTag("00181204"), ActionCodes.KEEP),  # Unknown
        (SingleTag("00181012"), ActionCodes.KEEP),  # DateOfSecondaryCapture
        (SingleTag("0040a120"), ActionCodes.KEEP),  # DateTime
        (SingleTag("00181202"), ActionCodes.KEEP),  # DateTimeOfLastCalibration
        (SingleTag("00189701"), ActionCodes.KEEP),  # DecayCorrectionDateTime
        (SingleTag("04000105"), ActionCodes.KEEP),  # DigitalSignatureDateTime
        (SingleTag("00380030"), ActionCodes.KEEP),  # DischargeDate
        (SingleTag("00380032"), ActionCodes.KEEP),  # DischargeTime
        (SingleTag("00686226"), ActionCodes.KEEP),  # EffectiveDateTime
        (SingleTag("00189517"), ActionCodes.KEEP),  # EndAcquisitionDateTime
        (
            SingleTag("00120087"),
            ActionCodes.KEEP,
        ),  # EthicsCommitteeApprovalEffectivenessEndDate
        (
            SingleTag("00120086"),
            ActionCodes.KEEP,
        ),  # EthicsCommitteeApprovalEffectivenessStartDate
        (SingleTag("00189804"), ActionCodes.KEEP),  # ExclusionStartDateTime
        (SingleTag("00404011"), ActionCodes.KEEP),  # ExpectedCompletionDateTime
        (SingleTag("0040a023"), ActionCodes.KEEP),  # FindingsGroupRecordingDateTrial
        (SingleTag("0040a024"), ActionCodes.KEEP),  # FindingsGroupRecordingTimeTrial
        (SingleTag("30080054"), ActionCodes.KEEP),  # FirstTreatmentDate
        (SingleTag("00189074"), ActionCodes.KEEP),  # FrameAcquisitionDateTime
        (SingleTag("00340007"), ActionCodes.KEEP),  # FrameOriginTimestamp
        (SingleTag("00189151"), ActionCodes.KEEP),  # FrameReferenceDateTime
        (SingleTag("00189623"), ActionCodes.KEEP),  # FunctionalSyncPulse
        (SingleTag("0016008d"), ActionCodes.KEEP),  # GPSDateStamp
        (SingleTag("0072000a"), ActionCodes.KEEP),  # HangingProtocolCreationDateTime
        (SingleTag("0040e004"), ActionCodes.KEEP),  # HL7DocumentEffectiveTime
        (SingleTag("003a0314"), ActionCodes.KEEP),  # ImpedanceMeasurementDateTime
        (SingleTag("00686270"), ActionCodes.KEEP),  # InformationIssueDateTime
        (SingleTag("00080015"), ActionCodes.KEEP),  # InstanceCoercionDateTime
        (SingleTag("00080012"), ActionCodes.KEEP),  # InstanceCreationDate
        (SingleTag("00080013"), ActionCodes.KEEP),  # InstanceCreationTime
        (SingleTag("00189919"), ActionCodes.KEEP),  # InstructionPerformedDateTime
        (SingleTag("30100085"), ActionCodes.KEEP),  # IntendedFractionStartTime
        (SingleTag("3010004d"), ActionCodes.KEEP),  # IntendedPhaseEndDate
        (SingleTag("3010004c"), ActionCodes.KEEP),  # IntendedPhaseStartDate
        (SingleTag("300a0741"), ActionCodes.KEEP),  # InterlockDateTime
        (SingleTag("40080112"), ActionCodes.KEEP),  # InterpretationApprovalDate
        (SingleTag("40080113"), ActionCodes.KEEP),  # InterpretationApprovalTime
        (SingleTag("40080100"), ActionCodes.KEEP),  # InterpretationRecordedDate
        (SingleTag("40080101"), ActionCodes.KEEP),  # InterpretationRecordedTime
        (SingleTag("40080108"), ActionCodes.KEEP),  # InterpretationTranscriptionDate
        (SingleTag("40080109"), ActionCodes.KEEP),  # InterpretationTranscriptionTime
        (SingleTag("00180035"), ActionCodes.KEEP),  # InterventionDrugStartTime
        (SingleTag("00180027"), ActionCodes.KEEP),  # InterventionDrugStopTime
        (SingleTag("00402004"), ActionCodes.KEEP),  # IssueDateOfImagingServiceRequest
        (SingleTag("00402005"), ActionCodes.KEEP),  # IssueTimeOfImagingServiceRequest
        (SingleTag("001021d0"), ActionCodes.KEEP),  # LastMenstrualDate
        (SingleTag("00203403"), ActionCodes.KEEP),  # ModifiedImageDate
        (SingleTag("00203405"), ActionCodes.KEEP),  # ModifiedImageTime
        (SingleTag("30080056"), ActionCodes.KEEP),  # MostRecentTreatmentDate
        (SingleTag("0040a192"), ActionCodes.KEEP),  # ObservationDateTrial
        (SingleTag("0040a032"), ActionCodes.KEEP),  # ObservationDateTime
        (SingleTag("0040a033"), ActionCodes.KEEP),  # ObservationStartDateTime
        (SingleTag("0040a193"), ActionCodes.KEEP),  # ObservationTimeTrial
        (SingleTag("00080024"), ActionCodes.KEEP),  # OverlayDate
        (SingleTag("00080034"), ActionCodes.KEEP),  # OverlayTime
        (SingleTag("300a0760"), ActionCodes.KEEP),  # OverrideDateTime
        (SingleTag("0040a082"), ActionCodes.KEEP),  # ParticipationDateTime
        (SingleTag("00400250"), ActionCodes.KEEP),  # PerformedProcedureStepEndDate
        (SingleTag("00404051"), ActionCodes.KEEP),  # PerformedProcedureStepEndDateTime
        (SingleTag("00400251"), ActionCodes.KEEP),  # PerformedProcedureStepEndTime
        (SingleTag("00400244"), ActionCodes.KEEP),  # PerformedProcedureStepStartDate
        (
            SingleTag("00404050"),
            ActionCodes.KEEP,
        ),  # PerformedProcedureStepStartDateTime
        (SingleTag("00400245"), ActionCodes.KEEP),  # PerformedProcedureStepStartTime
        (SingleTag("00700082"), ActionCodes.KEEP),  # PresentationCreationDate
        (SingleTag("00700083"), ActionCodes.KEEP),  # PresentationCreationTime
        (SingleTag("00404052"), ActionCodes.KEEP),  # ProcedureStepCancellationDateTime
        (SingleTag("0044000b"), ActionCodes.KEEP),  # ProductExpirationDateTime
        (SingleTag("00181078"), ActionCodes.KEEP),  # RadiopharmaceuticalStartDateTime
        (SingleTag("00181072"), ActionCodes.KEEP),  # RadiopharmaceuticalStartTime
        (SingleTag("00181079"), ActionCodes.KEEP),  # RadiopharmaceuticalStopDateTime
        (SingleTag("00181073"), ActionCodes.KEEP),  # RadiopharmaceuticalStopTime
        (SingleTag("300a073a"), ActionCodes.KEEP),  # RecordedRTControlPointDateTime
        (SingleTag("0040a13a"), ActionCodes.KEEP),  # ReferencedDateTime
        (SingleTag("300e0004"), ActionCodes.KEEP),  # ReviewDate
        (SingleTag("300e0005"), ActionCodes.KEEP),  # ReviewTime
        (SingleTag("3006002d"), ActionCodes.KEEP),  # Unknown
        (SingleTag("3006002e"), ActionCodes.KEEP),  # Unknown
        (SingleTag("300a0006"), ActionCodes.KEEP),  # RTPlanDate
        (SingleTag("300a0007"), ActionCodes.KEEP),  # RTPlanTime
        (SingleTag("30080162"), ActionCodes.KEEP),  # SafePositionExitDate
        (SingleTag("30080164"), ActionCodes.KEEP),  # SafePositionExitTime
        (SingleTag("30080166"), ActionCodes.KEEP),  # SafePositionReturnDate
        (SingleTag("30080168"), ActionCodes.KEEP),  # SafePositionReturnTime
        (SingleTag("0038001a"), ActionCodes.KEEP),  # ScheduledAdmissionDate
        (SingleTag("0038001b"), ActionCodes.KEEP),  # ScheduledAdmissionTime
        (SingleTag("0038001c"), ActionCodes.KEEP),  # ScheduledDischargeDate
        (SingleTag("0038001d"), ActionCodes.KEEP),  # ScheduledDischargeTime
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
        (SingleTag("00321000"), ActionCodes.KEEP),  # ScheduledStudyStartDate
        (SingleTag("00321001"), ActionCodes.KEEP),  # ScheduledStudyStartTime
        (SingleTag("00321010"), ActionCodes.KEEP),  # ScheduledStudyStopDate
        (SingleTag("00321011"), ActionCodes.KEEP),  # ScheduledStudyStopTime
        (SingleTag("00720061"), ActionCodes.KEEP),  # SelectorDAValue
        (SingleTag("00720063"), ActionCodes.KEEP),  # SelectorDTValue
        (SingleTag("0072006b"), ActionCodes.KEEP),  # SelectorTMValue
        (SingleTag("00080021"), ActionCodes.KEEP),  # SeriesDate
        (SingleTag("00080031"), ActionCodes.KEEP),  # SeriesTime
        (SingleTag("01000420"), ActionCodes.KEEP),  # SOPAuthorizationDateTime
        (SingleTag("0018936a"), ActionCodes.KEEP),  # SourceEndDateTime
        (SingleTag("00189369"), ActionCodes.KEEP),  # SourceStartDateTime
        (SingleTag("300a022c"), ActionCodes.KEEP),  # SourceStrengthReferenceDate
        (SingleTag("300a022e"), ActionCodes.KEEP),  # SourceStrengthReferenceTime
        (SingleTag("00189516"), ActionCodes.KEEP),  # StartAcquisitionDateTime
        (SingleTag("30060008"), ActionCodes.KEEP),  # StructureSetDate
        (SingleTag("30060009"), ActionCodes.KEEP),  # StructureSetTime
        (SingleTag("00321040"), ActionCodes.KEEP),  # StudyArrivalDate
        (SingleTag("00321041"), ActionCodes.KEEP),  # StudyArrivalTime
        (SingleTag("00321050"), ActionCodes.KEEP),  # StudyCompletionDate
        (SingleTag("00321051"), ActionCodes.KEEP),  # StudyCompletionTime
        (SingleTag("00080020"), ActionCodes.KEEP),  # StudyDate
        (SingleTag("00320034"), ActionCodes.KEEP),  # StudyReadDate
        (SingleTag("00320035"), ActionCodes.KEEP),  # StudyReadTime
        (SingleTag("00080030"), ActionCodes.KEEP),  # StudyTime
        (SingleTag("00320032"), ActionCodes.KEEP),  # StudyVerifiedDate
        (SingleTag("00320033"), ActionCodes.KEEP),  # StudyVerifiedTime
        (SingleTag("00440010"), ActionCodes.KEEP),  # SubstanceAdministrationDateTime
        (SingleTag("0040db07"), ActionCodes.KEEP),  # TemplateLocalVersion
        (SingleTag("0040db06"), ActionCodes.KEEP),  # TemplateVersion
        (SingleTag("0040a122"), ActionCodes.KEEP),  # Time
        (
            SingleTag("0040a112"),
            ActionCodes.KEEP,
        ),  # TimeOfDocumentCreationOrVerbalTransactionTrial
        (SingleTag("00181201"), ActionCodes.KEEP),  # TimeOfLastCalibration
        (SingleTag("0018700e"), ActionCodes.KEEP),  # TimeOfLastDetectorCalibration
        (SingleTag("00181014"), ActionCodes.KEEP),  # TimeOfSecondaryCapture
        (SingleTag("00080201"), ActionCodes.KEEP),  # TimezoneOffsetFromUTC
        (SingleTag("30080024"), ActionCodes.KEEP),  # TreatmentControlPointDate
        (SingleTag("30080025"), ActionCodes.KEEP),  # TreatmentControlPointTime
        (SingleTag("30080250"), ActionCodes.KEEP),  # TreatmentDate
        (SingleTag("30080251"), ActionCodes.KEEP),  # TreatmentTime
        (
            SingleTag("300a0736"),
            ActionCodes.KEEP,
        ),  # TreatmentToleranceViolationDateTime
        (SingleTag("0040a030"), ActionCodes.KEEP),  # VerificationDateTime
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
        (SingleTag("00440004"), ActionCodes.CLEAN),  # ApprovalStatusDateTime
        (SingleTag("00440104"), ActionCodes.CLEAN),  # AssertionDateTime
        (SingleTag("00440105"), ActionCodes.CLEAN),  # AssertionExpirationDateTime
        (SingleTag("04000562"), ActionCodes.CLEAN),  # AttributeModificationDateTime
        (SingleTag("300c0127"), ActionCodes.CLEAN),  # BeamHoldTransitionDateTime
        (SingleTag("0014407e"), ActionCodes.CLEAN),  # CalibrationDate
        (SingleTag("00181203"), ActionCodes.CLEAN),  # CalibrationDateTime
        (SingleTag("0014407c"), ActionCodes.CLEAN),  # CalibrationTime
        (SingleTag("04000310"), ActionCodes.CLEAN),  # CertifiedTimestamp
        (SingleTag("00080023"), ActionCodes.CLEAN),  # ContentDate
        (SingleTag("00080033"), ActionCodes.CLEAN),  # ContentTime
        (SingleTag("00080107"), ActionCodes.CLEAN),  # ContextGroupLocalVersion
        (SingleTag("00080106"), ActionCodes.CLEAN),  # ContextGroupVersion
        (SingleTag("00181042"), ActionCodes.CLEAN),  # ContrastBolusStartTime
        (SingleTag("00181043"), ActionCodes.CLEAN),  # ContrastBolusStopTime
        (SingleTag("0018a002"), ActionCodes.CLEAN),  # ContributionDateTime
        (SingleTag("21000040"), ActionCodes.CLEAN),  # CreationDate
        (SingleTag("21000050"), ActionCodes.CLEAN),  # CreationTime
        (SingleTag("00080025"), ActionCodes.CLEAN),  # CurveDate
        (SingleTag("00080035"), ActionCodes.CLEAN),  # CurveTime
        (SingleTag("0040a121"), ActionCodes.CLEAN),  # Date
        (
            SingleTag("0040a110"),
            ActionCodes.CLEAN,
        ),  # DateOfDocumentOrVerbalTransactionTrial
        (SingleTag("00181205"), ActionCodes.CLEAN),  # Unknown
        (SingleTag("00181200"), ActionCodes.CLEAN),  # DateOfLastCalibration
        (SingleTag("0018700c"), ActionCodes.CLEAN),  # DateOfLastDetectorCalibration
        (SingleTag("00181204"), ActionCodes.CLEAN),  # Unknown
        (SingleTag("00181012"), ActionCodes.CLEAN),  # DateOfSecondaryCapture
        (SingleTag("0040a120"), ActionCodes.CLEAN),  # DateTime
        (SingleTag("00181202"), ActionCodes.CLEAN),  # DateTimeOfLastCalibration
        (SingleTag("00189701"), ActionCodes.CLEAN),  # DecayCorrectionDateTime
        (SingleTag("04000105"), ActionCodes.CLEAN),  # DigitalSignatureDateTime
        (SingleTag("00380030"), ActionCodes.CLEAN),  # DischargeDate
        (SingleTag("00380032"), ActionCodes.CLEAN),  # DischargeTime
        (SingleTag("00686226"), ActionCodes.CLEAN),  # EffectiveDateTime
        (SingleTag("00189517"), ActionCodes.CLEAN),  # EndAcquisitionDateTime
        (
            SingleTag("00120087"),
            ActionCodes.CLEAN,
        ),  # EthicsCommitteeApprovalEffectivenessEndDate
        (
            SingleTag("00120086"),
            ActionCodes.CLEAN,
        ),  # EthicsCommitteeApprovalEffectivenessStartDate
        (SingleTag("00189804"), ActionCodes.CLEAN),  # ExclusionStartDateTime
        (SingleTag("00404011"), ActionCodes.CLEAN),  # ExpectedCompletionDateTime
        (SingleTag("0040a023"), ActionCodes.CLEAN),  # FindingsGroupRecordingDateTrial
        (SingleTag("0040a024"), ActionCodes.CLEAN),  # FindingsGroupRecordingTimeTrial
        (SingleTag("30080054"), ActionCodes.CLEAN),  # FirstTreatmentDate
        (SingleTag("00189074"), ActionCodes.CLEAN),  # FrameAcquisitionDateTime
        (SingleTag("00340007"), ActionCodes.CLEAN),  # FrameOriginTimestamp
        (SingleTag("00189151"), ActionCodes.CLEAN),  # FrameReferenceDateTime
        (SingleTag("00189623"), ActionCodes.CLEAN),  # FunctionalSyncPulse
        (SingleTag("0016008d"), ActionCodes.CLEAN),  # GPSDateStamp
        (SingleTag("0072000a"), ActionCodes.CLEAN),  # HangingProtocolCreationDateTime
        (SingleTag("0040e004"), ActionCodes.CLEAN),  # HL7DocumentEffectiveTime
        (SingleTag("003a0314"), ActionCodes.CLEAN),  # ImpedanceMeasurementDateTime
        (SingleTag("00686270"), ActionCodes.CLEAN),  # InformationIssueDateTime
        (SingleTag("00080015"), ActionCodes.CLEAN),  # InstanceCoercionDateTime
        (SingleTag("00080012"), ActionCodes.CLEAN),  # InstanceCreationDate
        (SingleTag("00080013"), ActionCodes.CLEAN),  # InstanceCreationTime
        (SingleTag("00189919"), ActionCodes.CLEAN),  # InstructionPerformedDateTime
        (SingleTag("30100085"), ActionCodes.CLEAN),  # IntendedFractionStartTime
        (SingleTag("3010004d"), ActionCodes.CLEAN),  # IntendedPhaseEndDate
        (SingleTag("3010004c"), ActionCodes.CLEAN),  # IntendedPhaseStartDate
        (SingleTag("300a0741"), ActionCodes.CLEAN),  # InterlockDateTime
        (SingleTag("40080112"), ActionCodes.CLEAN),  # InterpretationApprovalDate
        (SingleTag("40080113"), ActionCodes.CLEAN),  # InterpretationApprovalTime
        (SingleTag("40080100"), ActionCodes.CLEAN),  # InterpretationRecordedDate
        (SingleTag("40080101"), ActionCodes.CLEAN),  # InterpretationRecordedTime
        (SingleTag("40080108"), ActionCodes.CLEAN),  # InterpretationTranscriptionDate
        (SingleTag("40080109"), ActionCodes.CLEAN),  # InterpretationTranscriptionTime
        (SingleTag("00180035"), ActionCodes.CLEAN),  # InterventionDrugStartTime
        (SingleTag("00180027"), ActionCodes.CLEAN),  # InterventionDrugStopTime
        (SingleTag("00402004"), ActionCodes.CLEAN),  # IssueDateOfImagingServiceRequest
        (SingleTag("00402005"), ActionCodes.CLEAN),  # IssueTimeOfImagingServiceRequest
        (SingleTag("001021d0"), ActionCodes.CLEAN),  # LastMenstrualDate
        (SingleTag("00203403"), ActionCodes.CLEAN),  # ModifiedImageDate
        (SingleTag("00203405"), ActionCodes.CLEAN),  # ModifiedImageTime
        (SingleTag("30080056"), ActionCodes.CLEAN),  # MostRecentTreatmentDate
        (SingleTag("0040a192"), ActionCodes.CLEAN),  # ObservationDateTrial
        (SingleTag("0040a032"), ActionCodes.CLEAN),  # ObservationDateTime
        (SingleTag("0040a033"), ActionCodes.CLEAN),  # ObservationStartDateTime
        (SingleTag("0040a193"), ActionCodes.CLEAN),  # ObservationTimeTrial
        (SingleTag("00080024"), ActionCodes.CLEAN),  # OverlayDate
        (SingleTag("00080034"), ActionCodes.CLEAN),  # OverlayTime
        (SingleTag("300a0760"), ActionCodes.CLEAN),  # OverrideDateTime
        (SingleTag("0040a082"), ActionCodes.CLEAN),  # ParticipationDateTime
        (SingleTag("00400250"), ActionCodes.CLEAN),  # PerformedProcedureStepEndDate
        (SingleTag("00404051"), ActionCodes.CLEAN),  # PerformedProcedureStepEndDateTime
        (SingleTag("00400251"), ActionCodes.CLEAN),  # PerformedProcedureStepEndTime
        (SingleTag("00400244"), ActionCodes.CLEAN),  # PerformedProcedureStepStartDate
        (
            SingleTag("00404050"),
            ActionCodes.CLEAN,
        ),  # PerformedProcedureStepStartDateTime
        (SingleTag("00400245"), ActionCodes.CLEAN),  # PerformedProcedureStepStartTime
        (SingleTag("00700082"), ActionCodes.CLEAN),  # PresentationCreationDate
        (SingleTag("00700083"), ActionCodes.CLEAN),  # PresentationCreationTime
        (SingleTag("00404052"), ActionCodes.CLEAN),  # ProcedureStepCancellationDateTime
        (SingleTag("0044000b"), ActionCodes.CLEAN),  # ProductExpirationDateTime
        (SingleTag("00181078"), ActionCodes.CLEAN),  # RadiopharmaceuticalStartDateTime
        (SingleTag("00181072"), ActionCodes.CLEAN),  # RadiopharmaceuticalStartTime
        (SingleTag("00181079"), ActionCodes.CLEAN),  # RadiopharmaceuticalStopDateTime
        (SingleTag("00181073"), ActionCodes.CLEAN),  # RadiopharmaceuticalStopTime
        (SingleTag("300a073a"), ActionCodes.CLEAN),  # RecordedRTControlPointDateTime
        (SingleTag("0040a13a"), ActionCodes.CLEAN),  # ReferencedDateTime
        (SingleTag("300e0004"), ActionCodes.CLEAN),  # ReviewDate
        (SingleTag("300e0005"), ActionCodes.CLEAN),  # ReviewTime
        (SingleTag("3006002d"), ActionCodes.CLEAN),  # Unknown
        (SingleTag("3006002e"), ActionCodes.CLEAN),  # Unknown
        (SingleTag("300a0006"), ActionCodes.CLEAN),  # RTPlanDate
        (SingleTag("300a0007"), ActionCodes.CLEAN),  # RTPlanTime
        (SingleTag("30080162"), ActionCodes.CLEAN),  # SafePositionExitDate
        (SingleTag("30080164"), ActionCodes.CLEAN),  # SafePositionExitTime
        (SingleTag("30080166"), ActionCodes.CLEAN),  # SafePositionReturnDate
        (SingleTag("30080168"), ActionCodes.CLEAN),  # SafePositionReturnTime
        (SingleTag("0038001a"), ActionCodes.CLEAN),  # ScheduledAdmissionDate
        (SingleTag("0038001b"), ActionCodes.CLEAN),  # ScheduledAdmissionTime
        (SingleTag("0038001c"), ActionCodes.CLEAN),  # ScheduledDischargeDate
        (SingleTag("0038001d"), ActionCodes.CLEAN),  # ScheduledDischargeTime
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
        (SingleTag("00321000"), ActionCodes.CLEAN),  # ScheduledStudyStartDate
        (SingleTag("00321001"), ActionCodes.CLEAN),  # ScheduledStudyStartTime
        (SingleTag("00321010"), ActionCodes.CLEAN),  # ScheduledStudyStopDate
        (SingleTag("00321011"), ActionCodes.CLEAN),  # ScheduledStudyStopTime
        (SingleTag("00720061"), ActionCodes.CLEAN),  # SelectorDAValue
        (SingleTag("00720063"), ActionCodes.CLEAN),  # SelectorDTValue
        (SingleTag("0072006b"), ActionCodes.CLEAN),  # SelectorTMValue
        (SingleTag("00080021"), ActionCodes.CLEAN),  # SeriesDate
        (SingleTag("00080031"), ActionCodes.CLEAN),  # SeriesTime
        (SingleTag("01000420"), ActionCodes.CLEAN),  # SOPAuthorizationDateTime
        (SingleTag("0018936a"), ActionCodes.CLEAN),  # SourceEndDateTime
        (SingleTag("00189369"), ActionCodes.CLEAN),  # SourceStartDateTime
        (SingleTag("300a022c"), ActionCodes.CLEAN),  # SourceStrengthReferenceDate
        (SingleTag("300a022e"), ActionCodes.CLEAN),  # SourceStrengthReferenceTime
        (SingleTag("00189516"), ActionCodes.CLEAN),  # StartAcquisitionDateTime
        (SingleTag("30060008"), ActionCodes.CLEAN),  # StructureSetDate
        (SingleTag("30060009"), ActionCodes.CLEAN),  # StructureSetTime
        (SingleTag("00321040"), ActionCodes.CLEAN),  # StudyArrivalDate
        (SingleTag("00321041"), ActionCodes.CLEAN),  # StudyArrivalTime
        (SingleTag("00321050"), ActionCodes.CLEAN),  # StudyCompletionDate
        (SingleTag("00321051"), ActionCodes.CLEAN),  # StudyCompletionTime
        (SingleTag("00080020"), ActionCodes.CLEAN),  # StudyDate
        (SingleTag("00320034"), ActionCodes.CLEAN),  # StudyReadDate
        (SingleTag("00320035"), ActionCodes.CLEAN),  # StudyReadTime
        (SingleTag("00080030"), ActionCodes.CLEAN),  # StudyTime
        (SingleTag("00320032"), ActionCodes.CLEAN),  # StudyVerifiedDate
        (SingleTag("00320033"), ActionCodes.CLEAN),  # StudyVerifiedTime
        (SingleTag("00440010"), ActionCodes.CLEAN),  # SubstanceAdministrationDateTime
        (SingleTag("0040db07"), ActionCodes.CLEAN),  # TemplateLocalVersion
        (SingleTag("0040db06"), ActionCodes.CLEAN),  # TemplateVersion
        (SingleTag("0040a122"), ActionCodes.CLEAN),  # Time
        (
            SingleTag("0040a112"),
            ActionCodes.CLEAN,
        ),  # TimeOfDocumentCreationOrVerbalTransactionTrial
        (SingleTag("00181201"), ActionCodes.CLEAN),  # TimeOfLastCalibration
        (SingleTag("0018700e"), ActionCodes.CLEAN),  # TimeOfLastDetectorCalibration
        (SingleTag("00181014"), ActionCodes.CLEAN),  # TimeOfSecondaryCapture
        (SingleTag("00080201"), ActionCodes.CLEAN),  # TimezoneOffsetFromUTC
        (SingleTag("30080024"), ActionCodes.CLEAN),  # TreatmentControlPointDate
        (SingleTag("30080025"), ActionCodes.CLEAN),  # TreatmentControlPointTime
        (SingleTag("30080250"), ActionCodes.CLEAN),  # TreatmentDate
        (SingleTag("30080251"), ActionCodes.CLEAN),  # TreatmentTime
        (
            SingleTag("300a0736"),
            ActionCodes.CLEAN,
        ),  # TreatmentToleranceViolationDateTime
        (SingleTag("0040a030"), ActionCodes.CLEAN),  # VerificationDateTime
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
        (SingleTag("001811bb"), ActionCodes.CLEAN),  # AcquisitionFieldOfViewLabel
        (SingleTag("00189424"), ActionCodes.CLEAN),  # AcquisitionProtocolDescription
        (SingleTag("001021b0"), ActionCodes.CLEAN),  # AdditionalPatientHistory
        (SingleTag("00081084"), ActionCodes.CLEAN),  # AdmittingDiagnosesCodeSequence
        (SingleTag("00081080"), ActionCodes.CLEAN),  # AdmittingDiagnosesDescription
        (SingleTag("00102110"), ActionCodes.CLEAN),  # Allergies
        (SingleTag("006a0006"), ActionCodes.CLEAN),  # AnnotationGroupDescription
        (SingleTag("006a0005"), ActionCodes.CLEAN),  # AnnotationGroupLabel
        (SingleTag("300a00c3"), ActionCodes.CLEAN),  # BeamDescription
        (SingleTag("300a00dd"), ActionCodes.CLEAN),  # BolusDescription
        (SingleTag("00120072"), ActionCodes.CLEAN),  # ClinicalTrialSeriesDescription
        (SingleTag("00120051"), ActionCodes.CLEAN),  # ClinicalTrialTimePointDescription
        (SingleTag("00400310"), ActionCodes.CLEAN),  # CommentsOnRadiationDose
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
        (SingleTag("300a079a"), ActionCodes.CLEAN),  # DisplacementReferenceLabel
        (SingleTag("300a0016"), ActionCodes.CLEAN),  # DoseReferenceDescription
        (SingleTag("30100037"), ActionCodes.CLEAN),  # EntityDescription
        (SingleTag("30100035"), ActionCodes.CLEAN),  # EntityLabel
        (SingleTag("30100038"), ActionCodes.CLEAN),  # EntityLongLabel
        (SingleTag("30100036"), ActionCodes.CLEAN),  # EntityName
        (
            SingleTag("300a0676"),
            ActionCodes.CLEAN,
        ),  # EquipmentFrameOfReferenceDescription
        (SingleTag("003a032b"), ActionCodes.CLEAN),  # FilterLookupTableDescription
        (SingleTag("300a0196"), ActionCodes.CLEAN),  # FixationDeviceDescription
        (SingleTag("3010007f"), ActionCodes.CLEAN),  # FractionationNotes
        (SingleTag("300a0072"), ActionCodes.CLEAN),  # FractionGroupDescription
        (SingleTag("00209158"), ActionCodes.CLEAN),  # FrameComments
        (SingleTag("00084000"), ActionCodes.CLEAN),  # IdentifyingComments
        (SingleTag("00204000"), ActionCodes.CLEAN),  # ImageComments
        (SingleTag("00402400"), ActionCodes.CLEAN),  # ImagingServiceRequestComments
        (SingleTag("40080300"), ActionCodes.CLEAN),  # Impressions
        (SingleTag("300a0742"), ActionCodes.CLEAN),  # InterlockDescription
        (SingleTag("300a0783"), ActionCodes.CLEAN),  # InterlockOriginDescription
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
        (SingleTag("300a0794"), ActionCodes.CLEAN),  # PatientSetupPhotoDescription
        (SingleTag("00380500"), ActionCodes.CLEAN),  # PatientState
        (
            SingleTag("300a0792"),
            ActionCodes.CLEAN,
        ),  # PatientTreatmentPreparationMethodDescription
        (
            SingleTag("300a078e"),
            ActionCodes.CLEAN,
        ),  # PatientTreatmentPreparationProcedureParameterDescription
        (SingleTag("00400254"), ActionCodes.CLEAN),  # PerformedProcedureStepDescription
        (
            SingleTag("30020123"),
            ActionCodes.CLEAN,
        ),  # PositionAcquisitionTemplateDescription
        (SingleTag("30020121"), ActionCodes.CLEAN),  # PositionAcquisitionTemplateName
        (SingleTag("300a000e"), ActionCodes.CLEAN),  # PrescriptionDescription
        (SingleTag("3010007b"), ActionCodes.CLEAN),  # PrescriptionNotes
        (SingleTag("30100081"), ActionCodes.CLEAN),  # PrescriptionNotesSequence
        (SingleTag("30100061"), ActionCodes.CLEAN),  # PriorTreatmentDoseDescription
        (SingleTag("00181030"), ActionCodes.CLEAN),  # ProtocolName
        (SingleTag("00081088"), ActionCodes.CLEAN),  # PyramidDescription
        (SingleTag("00200027"), ActionCodes.CLEAN),  # PyramidLabel
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
        (SingleTag("04000565"), ActionCodes.CLEAN),  # ReasonForTheAttributeModification
        (SingleTag("00402001"), ActionCodes.CLEAN),  # ReasonForTheImagingServiceRequest
        (SingleTag("00401002"), ActionCodes.CLEAN),  # ReasonForTheRequestedProcedure
        (SingleTag("00321066"), ActionCodes.CLEAN),  # ReasonForVisit
        (SingleTag("00321067"), ActionCodes.CLEAN),  # ReasonForVisitCodeSequence
        (SingleTag("00400275"), ActionCodes.CLEAN),  # RequestAttributesSequence
        (SingleTag("00321070"), ActionCodes.CLEAN),  # RequestedContrastAgent
        (SingleTag("00401400"), ActionCodes.CLEAN),  # RequestedProcedureComments
        (SingleTag("00321060"), ActionCodes.CLEAN),  # RequestedProcedureDescription
        (SingleTag("00189937"), ActionCodes.CLEAN),  # RequestedSeriesDescription
        (
            SingleTag("00189185"),
            ActionCodes.CLEAN,
        ),  # RespiratoryMotionCompensationTechniqueDescription
        (SingleTag("40084000"), ActionCodes.CLEAN),  # ResultsComments
        (SingleTag("30060028"), ActionCodes.CLEAN),  # ROIDescription
        (SingleTag("30060038"), ActionCodes.CLEAN),  # ROIGenerationDescription
        (SingleTag("30060026"), ActionCodes.CLEAN),  # ROIName
        (SingleTag("30060088"), ActionCodes.CLEAN),  # ROIObservationDescription
        (SingleTag("30060085"), ActionCodes.CLEAN),  # ROIObservationLabel
        (SingleTag("3010005a"), ActionCodes.CLEAN),  # RTPhysicianIntentNarrative
        (SingleTag("300a0004"), ActionCodes.CLEAN),  # RTPlanDescription
        (SingleTag("300a0002"), ActionCodes.CLEAN),  # RTPlanLabel
        (SingleTag("300a0003"), ActionCodes.CLEAN),  # RTPlanName
        (SingleTag("30100054"), ActionCodes.CLEAN),  # RTPrescriptionLabel
        (SingleTag("300a062a"), ActionCodes.CLEAN),  # RTToleranceSetLabel
        (SingleTag("30100056"), ActionCodes.CLEAN),  # RTTreatmentApproachLabel
        (SingleTag("00400007"), ActionCodes.CLEAN),  # ScheduledProcedureStepDescription
        (SingleTag("00720066"), ActionCodes.CLEAN),  # SelectorLOValue
        (SingleTag("00720068"), ActionCodes.CLEAN),  # SelectorLTValue
        (SingleTag("0072006c"), ActionCodes.CLEAN),  # SelectorSHValue
        (SingleTag("0072006e"), ActionCodes.CLEAN),  # SelectorSTValue
        (SingleTag("00720070"), ActionCodes.CLEAN),  # SelectorUTValue
        (SingleTag("0008103e"), ActionCodes.CLEAN),  # SeriesDescription
        (SingleTag("00380062"), ActionCodes.CLEAN),  # ServiceEpisodeDescription
        (SingleTag("300a01b2"), ActionCodes.CLEAN),  # SetupTechniqueDescription
        (SingleTag("300a01a6"), ActionCodes.CLEAN),  # ShieldingDeviceDescription
        (SingleTag("00400602"), ActionCodes.CLEAN),  # SpecimenDetailedDescription
        (SingleTag("00400600"), ActionCodes.CLEAN),  # SpecimenShortDescription
        (SingleTag("30060006"), ActionCodes.CLEAN),  # StructureSetDescription
        (SingleTag("30060002"), ActionCodes.CLEAN),  # StructureSetLabel
        (SingleTag("30060004"), ActionCodes.CLEAN),  # StructureSetName
        (SingleTag("00324000"), ActionCodes.CLEAN),  # StudyComments
        (SingleTag("00081030"), ActionCodes.CLEAN),  # StudyDescription
        (SingleTag("300a0608"), ActionCodes.CLEAN),  # TreatmentPositionGroupLabel
        (SingleTag("30100077"), ActionCodes.CLEAN),  # TreatmentSite
        (SingleTag("300a000b"), ActionCodes.CLEAN),  # TreatmentSites
        (SingleTag("3010007a"), ActionCodes.CLEAN),  # TreatmentTechniqueNotes
        (
            SingleTag("300a0734"),
            ActionCodes.CLEAN,
        ),  # TreatmentToleranceViolationDescription
        (SingleTag("30100033"), ActionCodes.CLEAN),  # UserContentLabel
        (SingleTag("30100034"), ActionCodes.CLEAN),  # UserContentLongLabel
        (SingleTag("00384000"), ActionCodes.CLEAN),  # VisitComments
        (SingleTag("003a0329"), ActionCodes.CLEAN),  # WaveformFilterDescription
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
