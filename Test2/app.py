# Import Modules
import os.path

from flask import Flask, render_template, request

import model
import schema

# Create app and app.config to validate file types
app = Flask(__name__)
app.config["VALID_FILE"] = ["CSV"]


# Def function to validate filename
def valid_file(filename):
    if "." not in filename:
        return False

    extension = filename.rsplit(".", 1)[1]

    if extension.upper() in app.config["VALID_FILE"]:
        return True

    else:
        return False


# Def home function
@app.route("/")
def home():
    return render_template("record_amount.html")


# Def function that reads forms
@app.route("/", methods=["POST"])
def forms():
    # Create try except for defensive programming
    try:

        if request.files:
            file = request.files["file"]

            # If no filename is parsed generate csv
            if file.filename == "":

                record_count = int(request.form["record_count"])
                db_table_name = request.form["db_table"]
                csv_message = model.gen_csv(record_count)
                csv_import = schema.insert_db("output/output.csv", db_table_name)

                return render_template("record_amount.html", table_bod=csv_import, message=csv_message)

            # Elif file is valid insert into db and read from db
            elif valid_file(file.filename):
                file.save(os.path.join("imports/", file.filename))
                csv_import = schema.insert_db(f"imports/{file.filename}", file.filename)

                return render_template("record_amount.html", table_bod=csv_import, message="File Successfully Uploaded")

            # Return appropriate response
            else:

                return render_template("record_amount.html", message="File Is Not In A Valid Format")

    # Except ValueError and return appropriate response
    except ValueError:
        return render_template("record_amount.html", message="Value Cannot Contain Letters")


# Run app
if __name__ == '__main__':
    app.run(debug=True)
