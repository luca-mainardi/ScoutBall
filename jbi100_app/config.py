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

OUTFIELD_PLAYERS_STATS = []

STATS = {
    "gK": [
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
        "tackles",
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


# Not all the attributes are in the original dataset
GK_STATS = [
    "gk_clean_sheets_pct",
    "gk_saves_pct",
    "gk_pens_save_pct",
    "gk_passes_pct_launched",
    "gk_crosses_stopped_pct",
    "passes_pct",
]

DF_STATS = [
    "tacles_won/tackles",
    "dribble_tackles_pct",
    "aerial_won_pct",
    "block_passes_per_match",
    "block_shots_per_match",
    "passes_pct",
]

MF_STATS = [
    "Goals_assists_per_match",
    "sca_per_match",
    "dribbles_completed_pct",
    "tackles_won/tackles",
    "interceptions_per_match",
    "passes_pct",
]

FW_STATS = [
    "goals_assists_per_match",
    "sca_per_match",
    "dribbles_completed_pct",
    "shots_on_target_pct",
    "tackles_interceptions_per_match",
    "passes_pct",
]
