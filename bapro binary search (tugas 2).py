def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return mid

    return -1

flights = ["08:00", "11:30", "13.00", "14.45", "16.00", "18.25", "20.15"]

flight_to_find = input("Masukkan waktu penerbangan yang ingin dicari: ")

result = binary_search(flights, flight_to_find)

if result != -1:
    print(f"Waktu penerbangan ditemukan pada indeks: {result}")
else:
    print("Waktu penerbangan tidak ditemukan.")
