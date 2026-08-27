import { useEffect, useState } from "react";

function BookList() {
    const [books, setBooks] = useState([]);
    const [error, setError] = useState("");

    useEffect(() => {
        const fields = [
            "name",
            "book_title",
            "author",
            "status"
        ];

        fetch(
            "/api/resource/Book?fields=" +
            encodeURIComponent(JSON.stringify(fields)),
            {
                credentials: "include"
            }
        )
            .then(async (response) => {
                const data = await response.json();

                console.log("STATUS:", response.status);
                console.log("DATA:", data);

                if (!response.ok) {
                    throw new Error(
                        data.exception || "Failed to load books"
                    );
                }

                return data;
            })
            .then((data) => {
                setBooks(data.data || []);
            })
            .catch((error) => {
                console.error("Book error:", error);
                setError(error.message);
            });
    }, []);

    if (error) {
        return <div>Error loading books: {error}</div>;
    }

    return (
        <div>
            <h1>Books</h1>

            <button>Add Book</button>

            <table>
                <thead>
                    <tr>
                        <th>Title</th>
                        <th>Author</th>
                        <th>Status</th>
                    </tr>
                </thead>

                <tbody>
                    {books.map((book) => (
                        <tr key={book.name}>
                            <td>{book.book_title}</td>
                            <td>{book.author}</td>
                            <td>{book.status}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default BookList;