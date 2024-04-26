def main() -> None:
    try:
        # raise Exception("something went wrong")
        print("all worked out as expected")
    except Exception as exc:
        exc.extra_info = "maps are cool"
        # print(f"handled it! {exc}")
        # when have a raise without an argument,
        # it rethrows the original exception
        raise
    else:
        print("run more code if there is no exception")
    finally:
        print("runs no matter what, clean up code can go in here")

    print("continue as normal")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"error: {exc} {exc.extra_info}")
