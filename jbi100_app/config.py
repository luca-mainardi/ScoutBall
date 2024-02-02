POSITIONS = ["GK", "DF", "MF", "FW"]

NATIONALITIES = [
    "Argentina",
    "Australia",
    "Belgium",
    "Brazil",
    "Cameroon",
    "Canada",
    "Costa Rica",
    "Croatia",
    "Denmark",
    "Ecuador",
    "England",
    "France",
    "Germany",
    "Ghana",
    "IR Iran",
    "Japan",
    "Korea Republic",
    "Mexico",
    "Morocco",
    "Netherlands",
    "Poland",
    "Portugal",
    "Qatar",
    "Saudi Arabia",
    "Senegal",
    "Serbia",
    "Spain",
    "Switzerland",
    "Tunisia",
    "United States",
    "Uruguay",
    "Wales",
]

STATS = {
    "GK": [
        "gk_clean_sheets_pct",
        "gk_save_pct",
        "gk_pens_save_pct",
        "gk_passes_pct_launched",
        "gk_crosses_stopped_pct",
        "passes_pct",
    ],
    "DF": [
        "dribble_tackles_pct",
        "blocked_passes",
        "blocked_shots",
        "tackles_won_pct",
        "aerials_won_pct",
        "passes_pct",
    ],
    "MF": [
        "tackles_won_pct",
        "interceptions",
        "goals_assists_per90",
        "passes_pct",
        "dribbles_completed_pct",
        "sca_per90",
    ],
    "FW": [
        "tackles_interceptions",
        "goals_assists_per90",
        "passes_pct",
        "sca_per90",
        "dribbles_completed_pct",
        "shots_on_target_pct",
    ],
}

STATS_NAMES = {
    "GK": [
        "clean sheets pct",
        "save pct",
        "pen save pct",
        "passes launched pct",
        "crosses stopped pct",
        "passes pct",
    ],
    "DF": [
        "dribble tackles pct",
        "blocked passes",
        "blocked shots",
        "tackles won pct",
        "aerials won pct",
        "passes pct",
    ],
    "MF": [
        "tackles won pct",
        "interceptions",
        "goals assists per90",
        "passes pct",
        "dribbles completed pct",
        "sca per90",
    ],
    "FW": [
        "tackles interceptions",
        "goals assists per90",
        "passes pct",
        "sca per90",
        "dribbles completed pct",
        "shots on target pct",
    ],
}


# # Not all the attributes are in the original dataset
# GK_STATS = [
#     "gk_clean_sheets_pct",
#     "gk_saves_pct",
#     "gk_pens_save_pct",
#     "gk_passes_pct_launched",
#     "gk_crosses_stopped_pct",
#     "passes_pct",
# ]

# DF_STATS = [
#     "tacles_won/tackles",
#     "dribble_tackles_pct",
#     "aerial_won_pct",
#     "block_passes_per_match",
#     "block_shots_per_match",
#     "passes_pct",
# ]

# MF_STATS = [
#     "Goals_assists_per_match",
#     "sca_per_match",
#     "dribbles_completed_pct",
#     "tackles_won/tackles",
#     "interceptions_per_match",
#     "passes_pct",
# ]

# FW_STATS = [
#     "goals_assists_per_match",
#     "sca_per_match",
#     "dribbles_completed_pct",
#     "shots_on_target_pct",
#     "tackles_interceptions_per_match",
#     "passes_pct",
# ]
