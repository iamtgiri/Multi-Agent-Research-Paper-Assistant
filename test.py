from neo4j import GraphDatabase

def test_connection(uri, user, password):
    try:
        driver = GraphDatabase.driver(uri, auth=(user, password))
        with driver.session() as session:
            result = session.run("RETURN 1 AS num")
            record = result.single()
            print("✅ Neo4j connection successful:", record["num"])
    except Exception as e:
        print("❌ Connection failed:", e)

# Replace with your environment variables or hardcoded values
test_connection(
    "neo4j://127.0.0.1:7687",   # or bolt://localhost:7687 for local
    "neo4j",
    "Santanu@20"
)
