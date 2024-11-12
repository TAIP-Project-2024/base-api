from graph_drawing_repository import DrawingRepository
from graph_repository import GraphRepository

def main():
    drawing_repo = DrawingRepository()
    graph_repo = GraphRepository()

    # Example of working with graphs in GraphRepository
    with open("base-api/resources/graphs/example.graphml", "rb") as file:
        graph_id = graph_repo.add("ExampleGraph", file)
        print(f"Graph added with ID: {graph_id}")

    # Retrieve the graph and read the first few lines
    graph_file = graph_repo.get("ExampleGraph")
    if graph_file:
        print("Graph content preview:", graph_file[:500])

    # Update the graph with different content
    with open("base-api/resources/graphs/marvel.graphml", "rb") as file:
        graph_repo.update("ExampleGraph", file)
        print("Graph updated.")

    # Retrieve the graph and read the first few lines
    graph_file = graph_repo.get("ExampleGraph")
    if graph_file:
        print("Graph content preview:", graph_file[:500])

    # Delete the graph
    graph_repo.delete("ExampleGraph")
    print("Graph deleted.")

    # Example of working with drawings in DrawingRepository
    with open("base-api/resources/drawings/circular.html", "rb") as file:
        drawing_id = drawing_repo.add("ExampleDrawing", file)
        print(f"Drawing added with ID: {drawing_id}")

    # Retrieve the drawing and read the first few lines
    drawing_file = drawing_repo.get("ExampleDrawing")
    if drawing_file:
        print("Drawing content preview:", drawing_file[:500])

    # Update the drawing with different content
    with open("base-api/resources/drawings/simple_drawing.html", "rb") as file:
        drawing_repo.update("ExampleDrawing", file)
        print("Drawing updated.")

    # Retrieve the drawing and read the first few lines
    drawing_file = drawing_repo.get("ExampleDrawing")
    if drawing_file:
        print("Drawing content preview:", drawing_file[:500])

    # Delete the drawing
    drawing_repo.delete("ExampleDrawing")
    print("Drawing deleted.")

if __name__ == "__main__":
    main()
