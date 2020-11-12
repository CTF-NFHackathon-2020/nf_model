# Lines starting with # are comments featuring literature evidence.

EGFR Pathway
============

EGF binds to EGFR.
EGFR bound to EGF binds EGFR bound to EGF.
EGFR bound to EGFR phosphorylates itself at Y1016.
EGFR bound to EGFR phosphorylates itself at Y1069.
EGFR bound to EGFR phosphorylates itself at Y1092.
EGFR bound to EGFR phosphorylates itself at Y1110.
EGFR bound to EGFR phosphorylates itself at Y1138.
EGFR bound to EGFR phosphorylates itself at Y1172.
EGFR bound to EGFR phosphorylates itself at Y1197.

EGFR bound to EGFR phosphorylates SRC at Y419.
EGFR bound to EGFR phosphorylates SRC.
SRC phosphorylated at Y419 is active.

Active SRC phosphorylates EGFR at Y869.

IGF1R Pathway
=============

IGF1R binds IGF1R.
IGF1R bound to IGF1R phosphorylates itself at Y1166.
IGF1R phosphorylated at Y1166 is active.

Active IGF1R phosphorylates IRS1 at tyrosine.
Tyrosine-phosphorylated IRS1 is active.

Active IRS1 binds PIK3CA.

IRS1 phosphorylated at S312 is degraded.
Active PPP2CA dephosphorylates IRS1 at S312.
RPS6KB1 phosphorylates IRS1 at S312.

Adaptor proteins
================

# "From these studies, we concluded that Grb2 binds directly to the EGFR at
# Y-1068, to a lesser extent at Y-1086, and indirectly at Y-1173."
# "Both competition experiments with synthetic phosphopeptides and
# dephosphorylation protection analysis demonstrated that Y-1173 and Y-992 are
# major and minor binding sites, respectively, for Shc on the EGFR."
# 7518560

GRB2 binds EGFR phosphorylated on Y1092.
SHC1 binds EGFR phosphorylated on Y1197.
GRB2 binds SHC1 bound to EGFR.
GRB2 bound to EGFR translocates to the membrane.
GRB2 bound to SHC1 translocates to the membrane.

# "These results suggest a role for MAP kinase in the regulation of Grb2-Sos
# interactions."
# "We describe the identification of five MAP kinase sites (S-1137, S-1167,
# S-1178, S-1193, and S-1197) on hSos1."
# 8816480

Active MAPK1 phosphorylates SOS1 at S1178.
SOS1 not phosphorylated at S1178 binds to GRB2 at the membrane.
SOS1 bound to GRB2 translocates to the membrane.

SOS1 binds to IRS1 phosphorylated on tyrosine.
SOS1 bound to IRS1 translocates to the membrane.

SOS1 binds to EGFR phosphorylated on Y1110.
SOS1 bound to EGFR translocates to the membrane.

SOS1 at the membrane is active.

Ras-MAPK pathway
================

FNTA farnesylates KRAS.
FNTB farnesylates KRAS.

Farnesylated KRAS translocates to the membrane.
Active SOS1 activates KRAS that is at the membrane.
Active RASA1 inhibits KRAS that is at the membrane.

NF1 inhibits KRAS that is at the membrane.

Active KRAS binds BRAF.
Active KRAS binds RAF1.

# Raf activation

Active SRC phosphorylates BRAF bound to KRAS.
Active SRC phosphorylates RAF1 bound to KRAS.
Phosphorylated BRAF is active.
Phosphorylated RAF1 is active.
Active BRAF phosphorylates MAP2K1 at S218 and S222.
Active RAF1 phosphorylates MAP2K1 at S218 and S222.

MAP2K1 phosphorylated at S218 and S222 is active.

Active MAP2K1 phosphorylates MAPK1 at T185 and Y187.
MAPK1 phosphorylated at T185 and Y187 is active.

Active MAPK1 phosphorylates RPS6KA1 at T573 and T359.

Active AKT1 phosphorylates TSC2 on S939 and T1462.
PPP5C dephosphorylates TSC2 at S939.
RPS6KA1 phosphorylated at T573 is active.
Active RPS6KA1 phosphorylates TSC2 on S1798.

NF1 and NF2 interactions
========================

SPRED1 bound to NF1 is active.

# "We show that oncogenic EGFR (L858R) signaling leads to the phosphorylation
# of SPRED1 on serine 105, disrupting the SPRED1 and neurofibromin complex."
# 32697994
EGFR phosphorylates SPRED1 on S105.
EGFR L858R phosphorylates SPRED1 on S105.
NF1 binds SPRED1 not phosphorylated on S105.

NF1 binds DPYSL2.
NF1 binds VCP.
NF1 binds PTK2.

# "Merlin, through competitive binding to Angiomotin, releases Rich1 from the
# Angiomotin-inhibitory complex, allowing Rich1 to inactivate Rac1, ultimately
# leading to attenuation of Rac1 and Ras-MAPK pathways."
# "Merlin negatively regulates Rac1 activity and MAPK signaling by competing
# with Rich1 for Angiomotin binding."
# 21481793

# "Amot associates with Merlin and Rich1 at junctional structures and inhibits
Rac1 and downstream signaling into the MAPK pathway."
# 28464980

NF2 binds AMOT.

# "This analysis showed that Rich1 associates with polarity proteins. The most
# abundant Rich1-associated protein migrated at 85 kDa and yielded 31 peptides
# matching 46% of the sequence for Amot."
# 16678097

ARHGAP17 binds AMOT not bound to NF2.
ARHGAP17 not bound to AMOT inhibits RAC1.

# "Rich1 Is a GAP for Cdc42 that Associates with Tight Junctions in Epithelial
# Cells"
# 16678097

ARHGAP17 not bound to AMOT inhibits CDC42.

# "Binding of Pak to GTP-bound Cdc42 or Rac1 results in an increase in its
# kinase activity"
# 9989831
# https://www.nature.com/articles/1202361

# "Based on three-dimensional structure analysis, it has been suggested that
# inactive Pak is in a conformation in which the autoinhibitory domain interacts
# with the kinase domain. The binding of active Rac/cdc42 to Pak alleviates this
# inhibition and enables Pak activation. Once the inhibition is relieved, Pak
# undergoes autophosphorylation, and this prevents a conformational switch back
# into an inactive state."
# 14580336

PAK1 binds active CDC42.
PAK1 bound to CDC42 phosphorylates itself.
PAK1 binds active RAC1.
PAK1 bound to RAC1 phosphorylates itself.
Phosphorylated PAK1 is active.

# "Similarly, the neurofibromatosis type 2 (NF2) protein Merlin interacts with
# the N-terminal regulatory domain of PAK1 and inhibits Cdc42 and Rac1 stimulated
# kinase activity."
# 19465939

# "As shown in Figure 1B, GST-Pak1 bound to merlin, whereas GST alone did not.
# Thus, the interaction between Pak and merlin is likely to be direct."
# 14580336

# "While merlin and Pak1 could be coimmunoprecipitated under adherent growth
# conditions, the interaction between the two proteins was greatly enhanced when
# adhesion was lost (Figure 1D)."
# 14580336

# "NOTE: Could it therefore be that this interaction is primarily relevant in the
# cytosol when NF2 is free to bind PAK1?"

NF2 binds PAK1.

# "P21 activated kinase 1 (PAK), a downstream effector of Rac1, promotes the phosphorylation of merlin at S518 with conversion to an open conformation, initiating its degradation."
# 22567403

Active PAK1 phosphorylates NF2 at S518.
NF2 not phosphorylated at S518 is active.

# "Both cAMP-dependent protein kinase A (PKA) and Pak1 are able to phosphorylate
# Merlin at Ser518 and thereby inhibit its growth suppressive activity [ xref –
# xref ]."
# 19165420

PKA phosphorylates NF2 at S518.

# "In addition to PAK1, AKT phosphorylates merlin at Thr230 and Ser315, which
# promotes merlin degradation by proteasome."
# 20491622

AKT1 phosphorylates NF2 at T230 and S315.
NF2 phosphorylated at T230 and S315 is degraded.

Active NF2 binds MAP3K11.
CDC42 activates MAP3K11 not bound to NF2.

RAC1 activates Wnt.
KRAS leads to the phosphorylation of LRP6.

# "In the presence of Wnt3a-CM, activated PAK1 (p21 activated kinase) can bind
# to PIP 2 and phosphorylate Merlin on Ser 518, thus inducing the detachment of
# Merlin from LRP6 and allowing phosphorylation of LRP6 for the initiation of Wnt
# and beta-catenin signaling."
# 27345717

Phosphorylated LRP6 activates Wnt.

# "JNK is activated by Rac1 directly or via PAK1; however this process can be
# ameliorated in the presence of NF2"
# 23267122

# "Specifically, merlin overexpression suppresses Rac1 induced activation of
# c-Jun-N-terminal kinase (JNK) and AP-1 transcriptional activity, while loss of
# merlin results in the opposite."
# 18829550

RAC1 activates JNK.

SNAI1 not bound to NF2 binds TP53.
SNAI1 not bound to NF2 inhibits TP53.
TP53 inhibits cell cycle.

NF2 binds TP53BP2.
YAP1 binds SMAD3.
NF1 binds FBXW7.
FBXW7 ubiquitinates NF1.
Ubiquitinated NF1 is degraded.

NF2 binds DCAF1.

NF2 binds LATS1.
NF2 binds YAP1.
LATS1 phosphorylates YAP1 at S127.
14-3-3 proteins bind YAP1 phosphorylated at S127.
YAP1 not bound to 14-3-3 proteins translocates to the nucleus.
YAP1 in the nucleus binds to TEAD1.
TEAD1 bound to YAP1 is active.

NF2 binds LIMK2.
ROCK activates LIMK2 not bound to NF2.
LIMK2 phosphorylates Cofilin.

APP binds NF1.
GRB10 inhibits RAS.
NF2 binds CTNNA.
LAYN binds NF2.
NF1 binds DDAH1.
PKA phosphorylates NF1 bound to DDAH1.
JNK phosphorylates PXN at S178.
MDM2 binds TP53.
MDM2 ubiquitinates TP53.
Ubiquitinated TP53 is degraded.

PI-3-kinase and AKT pathway
===========================

# PI3K activation
# https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3128635/
# https://pubs.rsc.org/en/content/articlehtml/2019/cp/c9cp00101h
PIK3CA binds KRAS that is at the membrane.
PIK3CA bound to KRAS is active.

PIK3CA binds tyrosine-phosphorylated IRS1.
PIK3CA bound to IRS1 is active.

Active PIK3CA produces PIP3, while PTEN degrades PIP3.
PDPK1 binds to PIP3.
AKT1 binds to PIP3.
PDPK1 bound to PIP3 is active.
Active PDPK1 phosphorylates AKT1 at T308 bound to PIP3.
PPP2CA dephosphorylates AKT1 at T308.

Active DNAPK phosphorylates AKT1 at S473.
PHLPP1 and PHLPP2 dephosphorylate AKT1 at S473.

Active SRC phosphorylates AKT1 at Y315.

AKT1 phosphorylated at T308 is active.
AKT1 phosphorylated at Y315 is active.

Active AKT1 phosphorylates GSK3A at serine 21.
GSK3A not phosphorylated at serine 21 is active.

Active AKT1 phosphorylates GSK3B on S9 and S21.
GSK3B not phosphorylated on S21 is active.

Active GSK3B phosphorylates DPYSL2 on T514, T509, and S518.
DPYSL2 not phosphorylated on T514 binds Tubulin.
Tubulin not bound to DPYSL2 is degraded.
DPYSL2 binds STX1A.

MTOR
====

TSC2 not phosphorylated at S939, T1462, or S1798 binds TSC1.

TSC2 not bound to TSC1 is degraded.
TSC2 bound to TSC1 is active.
TSC1 bound to TSC2 is active.

Active TSC2 inhibits RHEB.
Active RHEB binds MTOR.

Active AKT1 phosphorylates MTOR at S2448.

MTOR not bound to AKT1S1 is active.
MTOR phosphorylated at S2448 is active.
MTOR bound to RHEB is active.

Active MTOR inhibits PPP2CA.

mTORC1
======

MTOR not bound to RICTOR binds to RPTOR.
Active MTOR bound to RPTOR phosphorylates RPS6KB1 at T412.
Active MTOR bound to RPTOR phosphorylates EIF4EBP1 at T37 and T70.

RPS6KB1 phosphorylated at T412 is active.
EIF4EBP1 not phosphorylated at T37 is active.

Active MAPK1 phosphorylates EIF4EBP1 at S65.

Active EIF4EBP1 inhibits EIF4E.
EIF4E increases translational initiation.
EIF4E increases cell proliferation.

mTORC2
======

MTOR not bound to RPTOR binds to RICTOR.
Active MTOR bound to RICTOR phosphorylates AKT1 at S473.

AKT1S1
======

Active AKT1 phosphorylates AKT1S1 at T246.
AKT1S1 phosphorylated at T246 binds 14-3-3 proteins.
AKT1S1 not bound to 14-3-3 proteins binds to MTOR.

MAPK substrates and effectors
=============================

Active MAPK1 phosphorylates ELK1 at S383 and S389.
ELK1 phosphorylated at S383 and S389 is active.
Active MAPK1 phosphorylates ETS1 at T38.
ETS1 phosphorylated at T38 is active.
Active MAPK1 phosphorylates CCND1 on T286.

# "Smad3 is phosphorylated by ERK MAP kinase upon EGF treatment. We have mapped
# the ERK phosphorylation sites to Ser 207, Ser 203, and Thr 178 in Smad3."
# 16156666

Active MAPK1 phosphorylates SMAD3.
Phosphorylated SMAD3 binds SMAD4.
SMAD3 bound to SMAD4 is active.

SRC substrates
==============

PTK2 phosphorylates itself on Y397.
SRC binds PTK2 phosphorylated on Y397.
SRC bound to PTK2 phosphorylates PTK2 on Y576, Y577, and Y925.
GRB2 binds to PTK2 phosphorylated on Y925.
GRB2 bound to PTK2 translocates to the membrane.

DUSPs
=====

Active MAPK1 phosphorylates DUSP6 on S159.

Induction of immediate early genes
==================================

ELK1 translocates to the nucleus.
Active ELK1 in the nucleus transcribes FOS.

PPP3CA dephosphorylates ELK1 at S383.
FOS binds to JUN.
FOS bound to JUN transcribes CCND1.
CCND1 binds to CDK4.
CDK4 bound to CCND1 phosphorylates RB1 at S807.
RB1 not phosphorylated at S807 is active.
Active RB1 inhibits cell proliferation.
Active RB1 inhibits cell cycle.

Downstream of mTOR
==================

Active MAPK1 phosphorylates RPS6KB1 at T444.
Active RPS6KB1 phosphorylates RPS6 at S235 and S240.
RPS6 phosphorylated at S235 and S240 is active.

Protein Kinase C
================

Active PRKCA phosphorylates GSK3A at serine 21.
Active PRKCA phosphorylates PEBP1 at S153.
Active PRKCA phosphorylates NF1 on serine.

Active RPS6KA1 phosphorylates RPS6 at S235.

Rac family GTPases
==================

Active SRC phosphorylates TIAM1.
Phosphorylated TIAM1 is active.
Active TIAM1 activates RAC1.

Miscellaneous
=============

Unphosphorylated PEBP1 binds RAF1.
RAF1 not bound to PEBP1 is active.

