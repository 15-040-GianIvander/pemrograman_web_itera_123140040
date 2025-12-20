from abc import ABC, abstractmethod
from typing import List, Optional


class LibraryItem(ABC):
    """
    Abstract base class untuk semua item perpustakaan.
    Memiliki id, judul, dan tahun terbit.
    """

    def __init__(self, item_id: int, title: str, year: int):
        self._id = item_id               # protected-ish (akses internal)
        self._title = title              # protected
        self._year = year                # protected

    @property
    def id(self) -> int:
        return self._id

    @property
    def title(self) -> str:
        # contoh penggunaan property decorator (read-only)
        return self._title

    @property
    def year(self) -> int:
        return self._year

    @abstractmethod
    def description(self) -> str:
        """Kembalikan deskripsi singkat item (harus diimplementasikan subclass)."""
        pass

    def __str__(self) -> str:
        """Polymorphism: setiap subclass dapat memodifikasi description()."""
        return f"[{self.id}] {self.title} ({self.year}) - {self.description()}"


class Book(LibraryItem):
    """
    Subclass untuk buku.
    Menambahkan: author dan publisher.
    Implementasi method abstract description().
    """

    def __init__(self, item_id: int, title: str, author: str, publisher: str, year: int, isbn: Optional[str] = None):
        super().__init__(item_id, title, year)
        self._author = author
        self._publisher = publisher
        self._isbn = isbn

    @property
    def author(self) -> str:
        return self._author

    @property
    def publisher(self) -> str:
        return self._publisher

    @property
    def isbn(self) -> Optional[str]:
        return self._isbn

    def description(self) -> str:
        isbn_part = f"ISBN:{self.isbn}" if self.isbn else "ISBN: -"
        return f"Buku oleh {self.author}, {self.publisher}, {isbn_part}"


class Magazine(LibraryItem):
    """
    Subclass untuk majalah.
    Menambahkan: volume dan issue.
    Implementasi method abstract description().
    """

    def __init__(self, item_id: int, title: str, volume: int, issue: int, year: int):
        super().__init__(item_id, title, year)
        self._volume = volume
        self._issue = issue

    @property
    def volume(self) -> int:
        return self._volume

    @property
    def issue(self) -> int:
        return self._issue

    def description(self) -> str:
        return f"Majalah - Vol.{self.volume} Issue {self.issue}"


class Library:
    """
    Class Library untuk menyimpan dan mengelola koleksi item.
    Menunjukkan encapsulation:
      - _items (protected) menyimpan daftar item
      - __id_counter (private) digunakan untuk memberi id unik otomatis
    """

    def __init__(self):
        self._items: List[LibraryItem] = []   # protected attribute
        self.__id_counter: int = 0            # private attribute

    def _next_id(self) -> int:
        """Private helper untuk membuat id unik."""
        self.__id_counter += 1
        return self.__id_counter

    def add_book(self, title: str, author: str, publisher: str, year: int, isbn: Optional[str] = None) -> Book:
        new_id = self._next_id()
        book = Book(new_id, title, author, publisher, year, isbn)
        self._items.append(book)
        return book

    def add_magazine(self, title: str, volume: int, issue: int, year: int) -> Magazine:
        new_id = self._next_id()
        mag = Magazine(new_id, title, volume, issue, year)
        self._items.append(mag)
        return mag

    def list_items(self) -> List[str]:
        """Mengembalikan list string representasi semua item yang ada."""
        return [str(item) for item in self._items]

    def find_by_id(self, item_id: int) -> Optional[LibraryItem]:
        """Cari item berdasarkan id; return None jika tidak ada."""
        for item in self._items:
            if item.id == item_id:
                return item
        return None

    def find_by_title(self, query: str) -> List[LibraryItem]:
        """
        Cari item berdasarkan judul (case-insensitive substring match).
        Mengembalikan daftar item yang cocok.
        """
        q = query.lower()
        results = [item for item in self._items if q in item.title.lower()]
        return results

    def remove_by_id(self, item_id: int) -> bool:
        """Hapus item berdasarkan id. Kembalikan True jika berhasil, False jika tidak ditemukan."""
        item = self.find_by_id(item_id)
        if item:
            self._items.remove(item)
            return True
        return False


# Contoh penggunaan (demo)
if __name__ == "__main__":
    lib = Library()

    # Menambah beberapa item
    lib.add_book(title="Python untuk Pemula", author="Andi", publisher="TechPress", year=2020, isbn="978-1-11-111111-1")
    lib.add_book(title="Belajar OOP di Python", author="Siti", publisher="EduMedia", year=2021)
    lib.add_magazine(title="Majalah Ilmu Komputer", volume=12, issue=4, year=2022)
    lib.add_magazine(title="Teknologi Hari Ini", volume=3, issue=1, year=2023)

    print("=== Daftar Semua Item ===")
    for line in lib.list_items():
        print(line)

    print("\n=== Cari Berdasarkan Judul 'python' ===")
    results = lib.find_by_title("python")
    if results:
        for r in results:
            print(r)
    else:
        print("Tidak ditemukan.")

    print("\n=== Cari Berdasarkan ID 2 ===")
    item = lib.find_by_id(2)
    if item:
        print("Ditemukan:", item)
    else:
        print("ID tidak ditemukan.")

    print("\n=== Menghapus ID 3 ===")
    ok = lib.remove_by_id(3)
    print("Hapus berhasil." if ok else "Hapus gagal (tidak ditemukan).")

    print("\n=== Daftar Setelah Hapus ===")
    for line in lib.list_items():
        print(line)
