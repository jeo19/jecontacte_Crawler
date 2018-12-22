#-*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import requests
from common import destoryPop, countPage, hasImg_products, get_Pinfo
import math
maxium=0
page=1
START_URL=['https://www.4mdmedical.com/medical-equipment/cabinetry.html'
, 'https://www.4mdmedical.com/medical-equipment/lighting/or-procedure.html'
, 'https://www.4mdmedical.com/medical-equipment/lighting/specialty.html'
, 'https://www.4mdmedical.com/medical-equipment/lighting/exam.html'
, 'https://www.4mdmedical.com/medical-equipment/lighting/loupes-headlamps.html'
, 'https://www.4mdmedical.com/medical-equipment/lighting/miscellaneous.html'
, 'https://www.4mdmedical.com/medical-equipment/stands.html'
, 'https://www.4mdmedical.com/medical-equipment/tables/bariatric.html'
, 'https://www.4mdmedical.com/medical-equipment/tables/exam.html'
, 'https://www.4mdmedical.com/medical-equipment/tables/pediatric-scale.html'
, 'https://www.4mdmedical.com/medical-equipment/tables/treatment.html'
, 'https://www.4mdmedical.com/medical-equipment/diagnostic-equipment/otoscope.html'
, 'https://www.4mdmedical.com/medical-equipment/diagnostic-equipment/pulse-oximeters-spirometers.html'
, 'https://www.4mdmedical.com/medical-equipment/diagnostic-equipment/illuminators.html'
, 'https://www.4mdmedical.com/medical-equipment/diagnostic-equipment/laryngoscopes.html'
, 'https://www.4mdmedical.com/medical-equipment/diagnostic-equipment/ultrasound.html'
, 'https://www.4mdmedical.com/medical-equipment/diagnostic-equipment/cardiology.html'
, 'https://www.4mdmedical.com/medical-equipment/diagnostic-equipment/dopplers.html'
, 'https://www.4mdmedical.com/medical-equipment/diagnostic-equipment/bmi-analyzer.html'
, 'https://www.4mdmedical.com/medical-equipment/diagnostic-equipment/microscopes.html'
, 'https://www.4mdmedical.com/medical-equipment/diagnostic-equipment/spirometry.html'
, 'https://www.4mdmedical.com/medical-equipment/radiology/protective-apparel.html'
, 'https://www.4mdmedical.com/medical-equipment/radiology/cassettes.html'
, 'https://www.4mdmedical.com/medical-equipment/radiology/storage.html'
, 'https://www.4mdmedical.com/medical-equipment/radiology/film.html'
, 'https://www.4mdmedical.com/medical-equipment/radiology/illuminators.html'
, 'https://www.4mdmedical.com/medical-equipment/radiology/miscellaneous.html'
, 'https://www.4mdmedical.com/medical-equipment/radiology/penlights.html'
, 'https://www.4mdmedical.com/medical-equipment/chairs-recliners-stools/step-stools.html'
, 'https://www.4mdmedical.com/medical-equipment/chairs-recliners-stools/recliners/pediatric-recliners.html'
, 'https://www.4mdmedical.com/medical-equipment/chairs-recliners-stools/recliners/tilt-and-recline-chairs.html'
, 'https://www.4mdmedical.com/medical-equipment/chairs-recliners-stools/recliners/3-position-recliners.html'
, 'https://www.4mdmedical.com/medical-equipment/chairs-recliners-stools/recliners/geri-chair-recliner.html'
, 'https://www.4mdmedical.com/medical-equipment/chairs-recliners-stools/recliners/bariatric-recliners.html'
, 'https://www.4mdmedical.com/medical-equipment/chairs-recliners-stools/recliners/recliner-parts-accessories.html'
, 'https://www.4mdmedical.com/medical-equipment/chairs-recliners-stools/gliders-and-rockers.html'
, 'https://www.4mdmedical.com/medical-equipment/chairs-recliners-stools/chairs.html'
, 'https://www.4mdmedical.com/medical-equipment/chairs-recliners-stools/stools.html'
, 'https://www.4mdmedical.com/medical-equipment/respiratory/accessories.html'
, 'https://www.4mdmedical.com/medical-equipment/respiratory/tracheostomy-products.html'
, 'https://www.4mdmedical.com/medical-equipment/respiratory/steam-mist-inhalers.html'
, 'https://www.4mdmedical.com/medical-equipment/respiratory/oxygen-cylinders-and-accessories.html'
, 'https://www.4mdmedical.com/medical-equipment/respiratory/miscellaneous.html'
, 'https://www.4mdmedical.com/medical-equipment/respiratory/ventilators.html'
, 'https://www.4mdmedical.com/medical-equipment/respiratory/airway-management.html'
, 'https://www.4mdmedical.com/medical-equipment/respiratory/aspirators.html'
, 'https://www.4mdmedical.com/medical-equipment/respiratory/disposable-products.html'
, 'https://www.4mdmedical.com/medical-equipment/respiratory/humidifiers.html'
, 'https://www.4mdmedical.com/medical-equipment/respiratory/oxygen-concentrators.html'
, 'https://www.4mdmedical.com/medical-equipment/respiratory/cpap-equipment.html'
, 'https://www.4mdmedical.com/medical-equipment/respiratory/oxygen-cylinders.html'
, 'https://www.4mdmedical.com/medical-equipment/respiratory/nebulizers-compressors.html'
, 'https://www.4mdmedical.com/medical-equipment/resident-room-furniture/pediatric-furniture.html'
, 'https://www.4mdmedical.com/medical-equipment/resident-room-furniture/visitor-furniture.html'
, 'https://www.4mdmedical.com/medical-equipment/resident-room-furniture/iv-poles.html'
, 'https://www.4mdmedical.com/medical-equipment/resident-room-furniture/televisions.html'
, 'https://www.4mdmedical.com/medical-equipment/resident-room-furniture/furnishings.html'
, 'https://www.4mdmedical.com/medical-equipment/resident-room-furniture/beds-1.html'
, 'https://www.4mdmedical.com/medical-equipment/resident-room-furniture/overbed-tables.html'
, 'https://www.4mdmedical.com/medical-equipment/resident-room-furniture/bedside-cabinets.html'
, 'https://www.4mdmedical.com/medical-equipment/patient-alarms-restraints/floor-pad-alarms.html'
, 'https://www.4mdmedical.com/medical-equipment/patient-alarms-restraints/pull-cord-alarms.html'
, 'https://www.4mdmedical.com/medical-equipment/patient-alarms-restraints/personal-alarms.html'
, 'https://www.4mdmedical.com/medical-equipment/patient-alarms-restraints/bed-alarms.html'
, 'https://www.4mdmedical.com/medical-equipment/patient-alarms-restraints/infrared-alarms.html'
, 'https://www.4mdmedical.com/medical-equipment/patient-alarms-restraints/chair-alarms.html'
, 'https://www.4mdmedical.com/medical-equipment/patient-alarms-restraints/doorway-alarms.html'
, 'https://www.4mdmedical.com/medical-equipment/lifts/slings.html'
, 'https://www.4mdmedical.com/medical-equipment/lifts/transfer-devices.html'
, 'https://www.4mdmedical.com/medical-equipment/lifts/transfer-devices.html'
, 'https://www.4mdmedical.com/medical-equipment/lifts/lifts.html'
, 'https://www.4mdmedical.com/medical-equipment/surgical-equipment/surgical-instruments-devices.html'
, 'https://www.4mdmedical.com/medical-equipment/surgical-equipment/warmers.html'
, 'https://www.4mdmedical.com/medical-equipment/surgical-equipment/surgical-lights.html'
, 'https://www.4mdmedical.com/medical-equipment/surgical-equipment/surgical-tables.html'
, 'https://www.4mdmedical.com/medical-equipment/stretchers/stretcher-accessories.html'
, 'https://www.4mdmedical.com/medical-equipment/stretchers/or-specialty-stretchers.html'
, 'https://www.4mdmedical.com/medical-equipment/stretchers/evacuation-chairs.html'
, 'https://www.4mdmedical.com/medical-equipment/stretchers/ambulance-cots.html'
, 'https://www.4mdmedical.com/medical-equipment/stretchers/transport-stretcher.html'
, 'https://www.4mdmedical.com/medical-equipment/stretchers/foldable-pole-stretchers.html'
, 'https://www.4mdmedical.com/medical-equipment/stretchers/splint-stretchers.html'
, 'https://www.4mdmedical.com/medical-equipment/carts/crash-carts.html'
, 'https://www.4mdmedical.com/medical-equipment/carts/miscellaneous.html'
, 'https://www.4mdmedical.com/medical-equipment/carts/specimen-collection-cart.html'
, 'https://www.4mdmedical.com/medical-equipment/carts/procedure-specialty.html'
, 'https://www.4mdmedical.com/medical-equipment/carts/case-carts.html'
, 'https://www.4mdmedical.com/medical-equipment/carts/laundry-linen-carts.html'
, 'https://www.4mdmedical.com/medical-equipment/carts/chart-holders-racks.html'
, 'https://www.4mdmedical.com/medical-equipment/carts/ekg-carts.html'
, 'https://www.4mdmedical.com/medical-equipment/carts/treatment-cart.html'
, 'https://www.4mdmedical.com/medical-equipment/carts/utility.html'
, 'https://www.4mdmedical.com/medical-equipment/carts/computer-stands.html'
, 'https://www.4mdmedical.com/medical-equipment/carts/anesthesia-cart.html'
, 'https://www.4mdmedical.com/medical-equipment/carts/medication-carts.html'
, 'https://www.4mdmedical.com/medical-equipment/carts/hospital-carts.html'
, 'https://www.4mdmedical.com/medical-equipment/miscellaneous.html'
, 'https://www.4mdmedical.com/daily-living-aids/reading-writing-aids/magnifiers.html'
, 'https://www.4mdmedical.com/daily-living-aids/reading-writing-aids/hand-aids.html'
, 'https://www.4mdmedical.com/daily-living-aids/visual-hearing-impaired-aids.html'
, 'https://www.4mdmedical.com/daily-living-aids/dining-aids/cups-drinking-aids.html'
, 'https://www.4mdmedical.com/daily-living-aids/dining-aids/feeders-arm-supports.html'
, 'https://www.4mdmedical.com/daily-living-aids/dining-aids/miscellaneous.html'
, 'https://www.4mdmedical.com/daily-living-aids/dining-aids/dining-accessories.html'
, 'https://www.4mdmedical.com/daily-living-aids/dining-aids/utensils.html'
, 'https://www.4mdmedical.com/daily-living-aids/dining-aids/plates-bowls.html'
, 'https://www.4mdmedical.com/daily-living-aids/dining-aids/kitchen-supplies.html'
, 'https://www.4mdmedical.com/daily-living-aids/dressing-aids/shoelaces-fasteners.html'
, 'https://www.4mdmedical.com/daily-living-aids/dressing-aids/dressing-education.html'
, 'https://www.4mdmedical.com/daily-living-aids/dressing-aids/slippers-socks.html'
, 'https://www.4mdmedical.com/daily-living-aids/dressing-aids/grooming-accessories.html'
, 'https://www.4mdmedical.com/daily-living-aids/dressing-aids/sock-stocking-aids.html'
, 'https://www.4mdmedical.com/daily-living-aids/dressing-aids/hip-kits.html'
, 'https://www.4mdmedical.com/daily-living-aids/dressing-aids/oral-care.html'
, 'https://www.4mdmedical.com/daily-living-aids/dressing-aids/medication-supplies.html'
, 'https://www.4mdmedical.com/daily-living-aids/dressing-aids/shoehorns.html'
, 'https://www.4mdmedical.com/daily-living-aids/dressing-aids/dressing-aids.html'
, 'https://www.4mdmedical.com/daily-living-aids/speech-communication/oral-motor-tools.html'
, 'https://www.4mdmedical.com/daily-living-aids/speech-communication/speech-assessments.html'
, 'https://www.4mdmedical.com/daily-living-aids/speech-communication/assistive-technology-speech-communication.html'
, 'https://www.4mdmedical.com/daily-living-aids/speech-communication/cognitive-assessments.html'
, 'https://www.4mdmedical.com/daily-living-aids/bath-toileting/brushes-scrub-sponges.html'
, 'https://www.4mdmedical.com/daily-living-aids/bath-toileting/bath-shower.html'
, 'https://www.4mdmedical.com/daily-living-aids/bath-toileting/hand-held-showers.html'
, 'https://www.4mdmedical.com/daily-living-aids/bath-toileting/bathing.html'
, 'https://www.4mdmedical.com/daily-living-aids/bath-toileting/mirrors-toileting-aids.html'
, 'https://www.4mdmedical.com/daily-living-aids/bath-toileting/commodes.html'
, 'https://www.4mdmedical.com/daily-living-aids/bath-toileting/toilet-aids.html'
, 'https://www.4mdmedical.com/daily-living-aids/bath-toileting/grab-bars-rails.html'
, 'https://www.4mdmedical.com/daily-living-aids/bath-toileting/miscellaneous.html'
, 'https://www.4mdmedical.com/daily-living-aids/home-accessories/household-helpers.html'
, 'https://www.4mdmedical.com/daily-living-aids/home-accessories/scissors.html'
, 'https://www.4mdmedical.com/daily-living-aids/home-accessories/automotive-aids.html'
, 'https://www.4mdmedical.com/daily-living-aids/home-accessories/mouth-sticks-head-pointers.html'
, 'https://www.4mdmedical.com/daily-living-aids/home-accessories/door-knob-turners.html'
, 'https://www.4mdmedical.com/daily-living-aids/home-accessories/trolleys-carts.html'
, 'https://www.4mdmedical.com/daily-living-aids/home-accessories/bedroom-aids.html'
, 'https://www.4mdmedical.com/daily-living-aids/home-accessories/furniture-risers.html'
, 'https://www.4mdmedical.com/daily-living-aids/home-accessories/telephones.html'
, 'https://www.4mdmedical.com/daily-living-aids/hygiene-products/oral-care.html'
, 'https://www.4mdmedical.com/daily-living-aids/hygiene-products/denture-care.html'
, 'https://www.4mdmedical.com/daily-living-aids/hygiene-products/shaving-cream.html'
, 'https://www.4mdmedical.com/daily-living-aids/medication-aids/pill-crushers.html'
, 'https://www.4mdmedical.com/daily-living-aids/medication-aids/pill-crushers.html'
, 'https://www.4mdmedical.com/daily-living-aids/low-vision/magnifiers.html'
, 'https://www.4mdmedical.com/daily-living-aids/low-vision/talking-devices.html'
, 'https://www.4mdmedical.com/daily-living-aids/miscellaneous-aids.html'
, 'https://www.4mdmedical.com/daily-living-aids/personal-care/grooming-supplies.html'
, 'https://www.4mdmedical.com/daily-living-aids/personal-care/urinals.html'
, 'https://www.4mdmedical.com/daily-living-aids/personal-care/hand-sanitizers.html'
, 'https://www.4mdmedical.com/daily-living-aids/personal-care/bedside-products.html'
, 'https://www.4mdmedical.com/daily-living-aids/personal-care/miscellaneous.html'
, 'https://www.4mdmedical.com/daily-living-aids/personal-care/cleansing.html'
, 'https://www.4mdmedical.com/daily-living-aids/personal-care/creams-ointments.html'
, 'https://www.4mdmedical.com/daily-living-aids/personal-care/oral-care.html'
, 'https://www.4mdmedical.com/daily-living-aids/personal-care/enemas.html'
, 'https://www.4mdmedical.com/daily-living-aids/personal-care/tissues.html'
, 'https://www.4mdmedical.com/daily-living-aids/environmental-controls.html'
, 'https://www.4mdmedical.com/daily-living-aids/adls.html'
, 'https://www.4mdmedical.com/daily-living-aids/scissors-book-holders-writing-aids/writing-aids.html'
, 'https://www.4mdmedical.com/daily-living-aids/scissors-book-holders-writing-aids/pen-pencil-aids.html'
, 'https://www.4mdmedical.com/daily-living-aids/scissors-book-holders-writing-aids/mouth-sticks-head-pointers.html'
, 'https://www.4mdmedical.com/daily-living-aids/scissors-book-holders-writing-aids/book-holders-page-turners.html'
, 'https://www.4mdmedical.com/daily-living-aids/scissors-book-holders-writing-aids/scissors.html'
, 'https://www.4mdmedical.com/daily-living-aids/reference-guides.html'
, 'https://www.4mdmedical.com/daily-living-aids/reachers.html'
, 'https://www.4mdmedical.com/laboratory/containers.html'
, 'https://www.4mdmedical.com/laboratory/hematology.html'
, 'https://www.4mdmedical.com/laboratory/lab-instrumentation.html'
, 'https://www.4mdmedical.com/laboratory/chemistry.html'
, 'https://www.4mdmedical.com/laboratory/neonatal-screening-products.html'
, 'https://www.4mdmedical.com/laboratory/urinalysis/analyzers.html'
, 'https://www.4mdmedical.com/laboratory/urinalysis/reagents-tests.html'
, 'https://www.4mdmedical.com/laboratory/microbiology-tests.html'
, 'https://www.4mdmedical.com/laboratory/sterilization.html'
, 'https://www.4mdmedical.com/laboratory/microbiology-products.html'
, 'https://www.4mdmedical.com/laboratory/plastic-bags.html'
, 'https://www.4mdmedical.com/laboratory/filter-papers-membranes.html'
, 'https://www.4mdmedical.com/laboratory/sample-collection-processing.html'
, 'https://www.4mdmedical.com/laboratory/coagulation/analyzers.html'
, 'https://www.4mdmedical.com/laboratory/miscellaneous-analyzers.html'
, 'https://www.4mdmedical.com/laboratory/point-of-care/hematology-analyzers.html'
, 'https://www.4mdmedical.com/laboratory/point-of-care/glucose-tests.html'
, 'https://www.4mdmedical.com/laboratory/point-of-care/hemoglobin-tests.html'
, 'https://www.4mdmedical.com/laboratory/point-of-care/rapid-tests.html'
, 'https://www.4mdmedical.com/laboratory/point-of-care/immunoassay-analyzers.html'
, 'https://www.4mdmedical.com/laboratory/point-of-care/cholesterol-tests.html'
, 'https://www.4mdmedical.com/laboratory/point-of-care/chemistry-analyzers.html'
, 'https://www.4mdmedical.com/laboratory/test-tubes-sealants.html'
, 'https://www.4mdmedical.com/laboratory/filtration-devices.html'
, 'https://www.4mdmedical.com/laboratory/blood-collection-products.html'
, 'https://www.4mdmedical.com/laboratory/miscellaneous.html'
, 'https://www.4mdmedical.com/laboratory/laboratory/autoclave-sterilizers.html'
, 'https://www.4mdmedical.com/laboratory/laboratory/loupes.html'
, 'https://www.4mdmedical.com/laboratory/binocular-loupes.html'
, 'https://www.4mdmedical.com/laboratory/glucose-a1c.html'
, 'https://www.4mdmedical.com/laboratory/lab-chemicals.html'
, 'https://www.4mdmedical.com/laboratory/microscopy/microscope-slides.html'
, 'https://www.4mdmedical.com/laboratory/microscopy/microscopes.html'
, 'https://www.4mdmedical.com/laboratory/microscopy/microscope-accessories.html'
, 'https://www.4mdmedical.com/laboratory/microscopy/microscope-coverslips.html'
, 'https://www.4mdmedical.com/more/janitorial-supplies.html'
, 'https://www.4mdmedical.com/more/dental.html'
, 'https://www.4mdmedical.com/more/veterinary.html'
, 'https://www.4mdmedical.com/ems-first-aid/spill-management.html'
, 'https://www.4mdmedical.com/ems-first-aid/burn-products.html'
, 'https://www.4mdmedical.com/ems-first-aid/cpr-resuscitators-bags.html'
, 'https://www.4mdmedical.com/ems-first-aid/mouth-teeth-care.html'
, 'https://www.4mdmedical.com/ems-first-aid/immobilizers.html'
, 'https://www.4mdmedical.com/ems-first-aid/head-immobilizers.html'
, 'https://www.4mdmedical.com/ems-first-aid/miscellaneous.html'
, 'https://www.4mdmedical.com/ems-first-aid/emergency-blankets.html'
, 'https://www.4mdmedical.com/ems-first-aid/airways-airways-kits.html'
, 'https://www.4mdmedical.com/ems-first-aid/first-aid-kits.html'
, 'https://www.4mdmedical.com/ems-first-aid/physician-bags.html'
, 'https://www.4mdmedical.com/ems-first-aid/epilepsy-bite-sticks.html'
, 'https://www.4mdmedical.com/ems-first-aid/straps.html'
, 'https://www.4mdmedical.com/ems-first-aid/e-m-t-supplies.html'
, 'https://www.4mdmedical.com/ems-first-aid/emergency-rescue.html'
, 'https://www.4mdmedical.com/ems-first-aid/eye-wash-protection.html'
, 'https://www.4mdmedical.com/ems-first-aid/ammonia-inhalants.html'
, 'https://www.4mdmedical.com/ems-first-aid/emergency-quick-splints.html'
, 'https://www.4mdmedical.com/ems-first-aid/fire-blanket.html'
, 'https://www.4mdmedical.com/ems-first-aid/cpr-boards.html'
, 'https://www.4mdmedical.com/ems-first-aid/cpr-masks.html'
, 'https://www.4mdmedical.com/ems-first-aid/back-boards.html'
, 'https://www.4mdmedical.com/ems-first-aid/rescue-response-bags.html'
, 'https://www.4mdmedical.com/ems-first-aid/portable-blanket-warming-system.html'
, 'https://www.4mdmedical.com/ems-first-aid/backboard-straps.html'
, 'https://www.4mdmedical.com/ems-first-aid/bags-kits.html'
, 'https://www.4mdmedical.com/ems-first-aid/emergency-instruments.html'
, 'https://www.4mdmedical.com/medical-equipment/scales/misc-scales.html'
, 'https://www.4mdmedical.com/medical-equipment/scales/scale-accessories.html'
, 'https://www.4mdmedical.com/medical-equipment/aed-defibrillators/electrode-lotions-gels.html'
, 'https://www.4mdmedical.com/medical-equipment/aed-defibrillators/aed-pads-and-electrodes.html'
, 'https://www.4mdmedical.com/medical-equipment/aed-defibrillators/aed-accessories.html'
, 'https://www.4mdmedical.com/medical-equipment/aed-defibrillators/aed-batteries.html'
, 'https://www.4mdmedical.com/medical-equipment/aed-defibrillators/aed-training-units.html'
, 'https://www.4mdmedical.com/medical-equipment/aed-defibrillators/signs-decals-posters.html'
, 'https://www.4mdmedical.com/medical-equipment/aed-defibrillators/aed-wall-cabinets.html'
, 'https://www.4mdmedical.com/medical-equipment/aed-defibrillators/electrodes.html'
, 'https://www.4mdmedical.com/medical-equipment/aed-defibrillators/aed-carrying-cases.html'
, 'https://www.4mdmedical.com/medical-equipment/aed-defibrillators/aed-defibrillators.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/pediatrics/mobility.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/pediatrics/bikes-and-helmets.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/pediatrics/toileting-bathing.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/pediatrics/seating-mobility.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/pediatrics/furniture.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/pediatrics/positioning.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/pediatrics/standers-gait-trainers.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/rehab-supplies/aquatic-therapy.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/rehab-supplies/storage.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/rehab-supplies/clinical-supplies.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/rehab-supplies/upper-extremity-exercise.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/rehab-supplies/reference.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/rehab-supplies/balance-total-body-conditioning.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/rehab-supplies/exercise-bands-tubing-balls-weights.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/rehab-supplies/lower-extremity-exercise-rebounders-flexibility.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/therapy-fitness/fitness-equipment.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/therapy-fitness/hot-cold-therapy.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/therapy-fitness/massage-therapy.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/therapy-fitness/walking-aides.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/therapy-fitness/therapy-room-essentials.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/therapy-fitness/personal-care-products.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/balance-total-body-conditioning.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/treatment-furniture/mat-platforms.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/treatment-furniture/treatment-tables.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/treatment-furniture/carts-stools.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/treatment-furniture/traction.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/treatment-furniture/rehab-equipment.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/treatment-furniture/exercise-hook-up-pole.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/treatment-furniture/work-activity-tables.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/orthopedics/back-supports.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/orthopedics/scar-management.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/orthopedics/knee-supports.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/orthopedics/finger-splints.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/orthopedics/upper-extremity-positioning.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/orthopedics/arthritis-supports.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/orthopedics/elbow-supports.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/orthopedics/cervical-collars.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/orthopedics/taping-products.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/orthopedics/shoulder-supports-slings.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/orthopedics/thumb-supports.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/orthopedics/compression-products.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/orthopedics/workhard-products.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/orthopedics/wound-care.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/soft-goods.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/exercise-equipment/strength-equipment.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/exercise-equipment/cardio-equipment.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/modalities/hot-cold-therapy.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/modalities/massage-wellness.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/modalities/iontophoresis.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/modalities/compression-therapy-products.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/modalities/hydrotherapy.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/modalities/biofeedback-pelvic-health.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/modalities/paraffin.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/modalities/electrotherapy-ultrasound.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/continuous-passive-motion.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/evaluation/range-of-motion.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/evaluation/assessments.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/evaluation/dexterity-sensory.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/evaluation/diagnostic-tools.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/evaluation/strength-testing.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/sensory-motor/balls.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/sensory-motor/vestibular-therapy.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/sensory-motor/visual-stimulation.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/sensory-motor/furniture.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/sensory-motor/relaxation.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/sensory-motor/manipulatives.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/sensory-motor/gross-motor.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/sensory-motor/tactile-stimulation.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/sensory-motor/sensory-development.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/splinting-casting/casting-fracture-bracing.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/splinting-casting/precuts.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/splinting-casting/dynamic-splinting.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/splinting-casting/preformed-splints.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/splinting-casting/strapping-material.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/splinting-casting/splinting-tools-materials-accessories.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/splinting-casting/padding-materials.html'
]
path = "chromedriver"
for goURL in START_URL:
    driver=destoryPop(goURL)#pop up destroy
    totalPN=countPage() #fetch total page number
    current_url=driver.current_url
    for page in range(1,totalPN+1):
        driver.get(current_url+"?p="+str(page))
        time.sleep(8)
        hasImg_urlList=hasImg_products() #Get URL list of products having img
        get_Pinfo(hasImg_urlList)