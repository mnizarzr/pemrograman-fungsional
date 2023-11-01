from functools import reduce

movies = [
    {"title": "Avengers: Endgame", "year": 2019, "rating": 8.4, "genre": "Action"},
    {"title": "Parasite", "year": 2019, "rating": 8.6, "genre": "Drama"},
    {"title": "Nomadland", "year": 2020, "rating": 7.3, "genre": "Drama"},
    {"title": "Dune", "year": 2021, "rating": 7.9, "genre": "Sci-Fi"},
    {
        "title": "Spider-Man: No Way Home",
        "year": 2021,
        "rating": 7.6,
        "genre": "Action",
    },
    {"title": "The French Dispatch", "year": 2021, "rating": 7.0, "genre": "Comedy"},
    {"title": "A Quiet Place Part II", "year": 2020, "rating": 7.4, "genre": "Horror"},
    {"title": "No Time to Die", "year": 2021, "rating": 6.8, "genre": "Action"},
    {"title": "The Power of the Dog", "year": 2021, "rating": 7.3, "genre": "Drama"},
    {"title": "Eternals", "year": 2021, "rating": 6.4, "genre": "Action"},
    {"title": "The Last Duel", "year": 2021, "rating": 7.0, "genre": "Drama"},
]


def count_movies_by_genre(movies):
    genre_counts = {}
    genres = list(map(lambda m: m["genre"], movies))
    unique_genres = set(genres)
    genre_counts = reduce(
        lambda acc, genre: {**acc, genre: genres.count(genre)}, unique_genres, {}
    )
    return genre_counts


def calculate_average_rating_by_year(movies):
    years = list(map(lambda m: m["year"], movies))
    ratings = list(map(lambda m: m["rating"], movies))
    unique_years = set(years)
    average_ratings = reduce(
        lambda acc, year: {
            **acc,
            year: sum([ratings[i] for i in range(len(movies)) if years[i] == year])
            / years.count(year),
        },
        unique_years,
        {},
    )
    return average_ratings


find_highest_rated_movie = lambda movies: max(movies, key=lambda m: m["rating"])
find_movie_by_title = lambda title, movies: list(
    filter(lambda m: title.lower() in m["title"].lower(), movies)
)


def main():
    global movies
    while True:
        print("\nPilih tugas yang ingin dilakukan:")
        print("1. Menghitung jumlah film berdasarkan genre")
        print("2. Menghitung rata-rata rating film berdasarkan tahun rilis")
        print("3. Menemukan film dengan rating tertinggi")
        print(
            "4. Cari judul film untuk menampilkan informasi rating, tahun rilis, dan genre"
        )
        print("5. Selesai")

        choice = input("Masukkan nomor tugas (1/2/3/4/5): ")

        if choice == "1":
            genres = count_movies_by_genre(movies)
            print("Jumlah Film Berdasarkan Genre: ", genres)
        elif choice == "2":
            ratings = calculate_average_rating_by_year(movies)
            print("Rata-rata Rating Film Berdasarkan Tahun Rilis: ", ratings)
        elif choice == "3":
            highest = find_highest_rated_movie(movies)
            print("Film dengan Rating Tertinggi:")
            print("\nInformasi Film:", highest["title"])
            print("Rating:", highest["rating"])
            print("Tahun Rilis:", highest["year"])
            print("Genre:", highest["genre"])
        elif choice == "4":
            title = input("Masukkan judul film yang ingin dicari: ")
            found_movie = find_movie_by_title(title, movies)
            if found_movie:
                found_movie = found_movie[0]
                print("\nInformasi Film:", found_movie["title"])
                print("Rating:", found_movie["rating"])
                print("Tahun Rilis:", found_movie["year"])
                print("Genre:", found_movie["genre"])
            else:
                print("Film dengan judul tersebut tidak ditemukan.")
        elif choice == "5":
            break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
