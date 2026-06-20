import sqlite3

conn = sqlite3.connect(
    "resume_analysis.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS analysis_history (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    resume_name TEXT,

    ats_score TEXT,

    analysis TEXT,

    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP

)
""")

conn.commit()


def save_analysis(
    resume_name,
    ats_score,
    analysis
):

    cursor.execute(
        """
        INSERT INTO analysis_history
        (
            resume_name,
            ats_score,
            analysis
        )
        VALUES
        (
            ?,
            ?,
            ?
        )
        """,
        (
            resume_name,
            ats_score,
            analysis
        )
    )

    conn.commit()


def get_history():

    cursor.execute(
        """
        SELECT
        resume_name,
        ats_score,
        timestamp
        FROM analysis_history
        ORDER BY id DESC
        """
    )

    return cursor.fetchall()