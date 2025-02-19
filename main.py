# Movie Database Manager

MOVIE_FILE = "movies.txt"

def read_movies():
    """Reads movies from the file and returns a list of movie records."""
    try:
        with open(MOVIE_FILE, "r", encoding="ISO-8859-1") as file:
            return [line.strip().split(";") for line in file.readlines()]
    except FileNotFoundError:
        print("Error: The file was not found.")
        return []

def write_movies(movies):
    """Writes the list of movies back to the file."""
    with open(MOVIE_FILE, "w", encoding="ISO-8859-1") as file:
        for movie in movies:
            file.write(";".join(movie) + "\n")

def add_movie():
    """Adds a new movie to the database."""
    title = input("Enter the movie title: ")
    movie_type = input("Enter the movie type (Feature Film, TV Series, etc.): ")
    director = input("Enter the director's name: ")
    rating = input("Enter the IMDb rating: ")
    duration = input("Enter the duration in minutes: ")
    year = input("Enter the release year: ")
    genre = input("Enter the genre (comma-separated): ")
    votes = input("Enter the number of votes: ")
    movies = read_movies()
    movies.append([title, movie_type, director, rating, duration, year, genre, votes, " ", " ", " "])
    write_movies(movies)
    print(f"Movie '{title}' added successfully.")

def search_movie():
    """Searches for a movie by title or director."""
    query = input("Enter the title or director to search for: ").lower()
    movies = read_movies()
    results = [movie for movie in movies if query in movie[0].lower() or query in (movie[2] or "").lower()]
    if results:
        print("Movies found:")
        for movie in results:
            print(f"Title: {movie[0]}, Director: {movie[2]}, Year: {movie[5]}, Rating: {movie[3]}")
    else:
        print("No movies found.")

def filter_movies():
    """Filters movies based on genre, year, or IMDb rating."""
    filter_type = input("Filter by genre, year, or rating? ").strip().lower()
    movies = read_movies()
    if filter_type == "genre":
        genre = input("Enter the genre to filter by: ").strip().lower()
        results = [movie for movie in movies if genre in movie[6].lower()]
    elif filter_type == "year":
        year = input("Enter the release year to filter by: ")
        results = [movie for movie in movies if movie[5] == year]
    elif filter_type == "rating":
        min_rating = float(input("Enter the minimum rating: "))
        results = [movie for movie in movies if float(movie[3]) >= min_rating]
    else:
        print("Invalid filter type.")
        return
    if results:
        print("Filtered movies:")
        for movie in results:
            print(f"Title: {movie[0]}, Year: {movie[5]}, Rating: {movie[3]}")
    else:
        print("No movies matched the criteria.")

def update_movie():
    """Updates movie details."""
    title = input("Enter the title of the movie to update: ").lower()
    movies = read_movies()
    for movie in movies:
        if movie[0].lower() == title:
            print(f"Current details: {movie}")
            movie[3] = input(f"Enter new IMDb rating (current: {movie[3]}): ") or movie[3]
            movie[4] = input(f"Enter new duration (current: {movie[4]}): ") or movie[4]
            write_movies(movies)
            print(f"Movie '{movie[0]}' updated successfully.")
            return
    print("Movie not found.")

def analyze_movies():
    """Analyze and display statistics about the movie database."""
    movies = read_movies()

    # Filter out empty or non-numeric ratings
    ratings = [float(movie[3]) for movie in movies if movie[3].strip().replace('.', '').isdigit()]
    
    if ratings:
        average_rating = sum(ratings) / len(ratings)
        print(f"Average IMDb Rating: {average_rating:.2f}")
    else:
        print("No valid ratings available.")

    # Most common genre calculation
    genres = []
    for movie in movies:
        genres.extend(movie[6].split(",") if movie[6].strip() else [])
    
    if genres:
        most_common_genre = max(set(genres), key=genres.count)
        print(f"Most Common Genre: {most_common_genre}")
    else:
        print("No genres available.")

    # Longest and shortest movies based on duration
    durations = [(movie[0], int(movie[4])) for movie in movies if movie[4].strip().isdigit()]

    if durations:
        longest_movie = max(durations, key=lambda x: x[1])
        shortest_movie = min(durations, key=lambda x: x[1])
        print(f"Longest Movie: {longest_movie[0]} ({longest_movie[1]} min)")
        print(f"Shortest Movie: {shortest_movie[0]} ({shortest_movie[1]} min)")
    else:
        print("No valid durations available.")

# Main Menu
def main():
    while True:
        print("\nMovie Database Manager")
        print("1. Add a new movie")
        print("2. Search for a movie")
        print("3. Filter movies")
        print("4. Update movie details")
        print("5. Analyze movie data")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            add_movie()
        elif choice == "2":
            search_movie()
        elif choice == "3":
            filter_movies()
        elif choice == "4":
            update_movie()
        elif choice == "5":
            analyze_movies()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
