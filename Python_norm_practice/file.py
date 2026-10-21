def write_log(message):
    with open(r"C:\Python_practice\app.log", "a") as file:
        file.write(message + "\n")

write_log("App Started")
write_log("App is working")
write_log("App Stopped")