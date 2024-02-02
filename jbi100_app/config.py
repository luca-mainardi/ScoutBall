"""
This file contains constants used in the app
"""

# List of positions
POSITIONS = ["GK", "DF", "MF", "FW"]

# List of nationalities in the dataset
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

# Dictionary for names of attributes in the dataset, for each position
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

# Dictionary for names of stats, for labels in the sidebar
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
