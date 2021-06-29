import json
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)

# There is a concept of Cross-Origin in case of APIs’.
# It means that even if we have developed our API with python,
# Other origins(languages like Javascript, React) can also
# access our API. So, we will also import CORS and assign
# our app as an CORS app.
CORS(app)

# Read the JSON data file
json_file_path = r"GRM_Projects_Data.json"
with open(json_file_path) as f:
    db = json.load(f)


@app.route("/")
def index():
    return """
            <h1>Welcome to Global Restoration Monitor API 1.0</h1>
            <h2> Try the below endpoints:</h2>
            <li> <a href="https://grm-api-v1.herokuapp.com/projects">Retrieve all projects.</a>
            <li> <a href="https://grm-api-v1.herokuapp.com/projects/1">Retrieve a project's information given the project ID.</a>
            """


@app.route("/projects", methods=["GET"])
def get_all_projects():
    return {"PROJECTS": db}


@app.route("/projects", methods=["POST"])
def add_project():
    __OBJECTID = request.form.get("__OBJECTID")
    Budget = request.form.get("Budget")
    C02e_To_Date = request.form.get("C02e_To_Date")
    Description = request.form.get("Description")
    DirectBeneficiaries_HH = request.form.get("DirectBeneficiaries_HH")
    District = request.form.get("District")
    Donor_Principal = request.form.get("Donor_Principal")
    Donors_Other = request.form.get("Donors_Other")
    End_Year = request.form.get("End_Year")
    Implementing_Partners = request.form.get("Implementing_Partners")
    InDirectBeneficiaries_HH = request.form.get("InDirectBeneficiaries_HH")
    Land_Area = request.form.get("Land_Area")
    Logo = request.form.get("Logo")
    Men_Trained = request.form.get("Men_Trained")
    Nation = request.form.get("Nation")
    Organisation = request.form.get("Organisation")
    People_Trained = request.form.get("People_Trained")
    Practice = request.form.get("Practice")
    Proj_Code = request.form.get("Proj_Code")
    Proj_Currency = request.form.get("Proj_Currency")
    Proj_Status = request.form.get("Proj_Status")
    Project_Description = request.form.get("Project_Description")
    Project_Value = request.form.get("Project_Value")
    Site_Code = request.form.get("Site_Code")
    Start_Year = request.form.get("Start_Year")
    Tree_Density = request.form.get("Tree_Density")
    Trees_mgmt = request.form.get("Trees_mgmt")
    Video = request.form.get("Video")
    x = request.form.get("x")
    y = request.form.get("y")

    if __OBJECTID:
        new_project = {
            __OBJECTID: {
                "__OBJECTID": __OBJECTID,
                "Budget": Budget,
                "C02e_To_Date": C02e_To_Date,
                "Description": Description,
                "DirectBeneficiaries_HH": DirectBeneficiaries_HH,
                "District": District,
                "Donor_Principal": Donor_Principal,
                "Donors_Other": Donors_Other,
                "End_Year": End_Year,
                "Implementing_Partners": Implementing_Partners,
                "InDirectBeneficiaries_HH": InDirectBeneficiaries_HH,
                "Land_Area": Land_Area,
                "Logo": Logo,
                "Men_Trained": Men_Trained,
                "Nation": Nation,
                "Organisation": Organisation,
                "People_Trained": People_Trained,
                "Practice": Practice,
                "Proj_Code": Proj_Code,
                "Proj_Currency": Proj_Currency,
                "Proj_Status": Proj_Status,
                "Project_Description": Project_Description,
                "Project_Value": Project_Value,
                "Site_Code": Site_Code,
                "Start_Year": Start_Year,
                "Tree_Density": Tree_Density,
                "Trees_mgmt": Trees_mgmt,
                "Video": Video,
                "x": x,
                "y": y,
            }
        }

        db[__OBJECTID] = new_project
        return {"NEW PROJECT CREATED!": new_project}
    else:
        return "__OBJECTID IS REQUIRED!"


@app.route("/projects/<__OBJECTID>", methods=["GET"])
def get_project(__OBJECTID):
    if __OBJECTID in db.keys():
        return {__OBJECTID: db[__OBJECTID]}
    else:
        return "<h1>PROJECT ID {} IS NOT FOUND!</h1>".format(__OBJECTID)


@app.route("/projects/<__OBJECTID>", methods=["PUT"])
def update_project(__OBJECTID):
    if __OBJECTID in db.keys():
        Budget = request.form.get("Budget")
        C02e_To_Date = request.form.get("C02e_To_Date")
        Description = request.form.get("Description")
        DirectBeneficiaries_HH = request.form.get("DirectBeneficiaries_HH")
        District = request.form.get("District")
        Donor_Principal = request.form.get("Donor_Principal")
        Donors_Other = request.form.get("Donors_Other")
        End_Year = request.form.get("End_Year")
        Implementing_Partners = request.form.get("Implementing_Partners")
        InDirectBeneficiaries_HH = request.form.get("InDirectBeneficiaries_HH")
        Land_Area = request.form.get("Land_Area")
        Logo = request.form.get("Logo")
        Men_Trained = request.form.get("Men_Trained")
        Nation = request.form.get("Nation")
        Organisation = request.form.get("Organisation")
        People_Trained = request.form.get("People_Trained")
        Practice = request.form.get("Practice")
        Proj_Code = request.form.get("Proj_Code")
        Proj_Currency = request.form.get("Proj_Currency")
        Proj_Status = request.form.get("Proj_Status")
        Project_Description = request.form.get("Project_Description")
        Project_Value = request.form.get("Project_Value")
        Site_Code = request.form.get("Site_Code")
        Start_Year = request.form.get("Start_Year")
        Tree_Density = request.form.get("Tree_Density")
        Trees_mgmt = request.form.get("Trees_mgmt")
        Video = request.form.get("Video")
        x = request.form.get("x")
        y = request.form.get("y")

        updates = {
            "Budget": Budget,
            "C02e_To_Date": C02e_To_Date,
            "Description": Description,
            "DirectBeneficiaries_HH": DirectBeneficiaries_HH,
            "District": District,
            "Donor_Principal": Donor_Principal,
            "Donors_Other": Donors_Other,
            "End_Year": End_Year,
            "Implementing_Partners": Implementing_Partners,
            "InDirectBeneficiaries_HH": InDirectBeneficiaries_HH,
            "Land_Area": Land_Area,
            "Logo": Logo,
            "Men_Trained": Men_Trained,
            "Nation": Nation,
            "Organisation": Organisation,
            "People_Trained": People_Trained,
            "Practice": Practice,
            "Proj_Code": Proj_Code,
            "Proj_Currency": Proj_Currency,
            "Proj_Status": Proj_Status,
            "Project_Description": Project_Description,
            "Project_Value": Project_Value,
            "Site_Code": Site_Code,
            "Start_Year": Start_Year,
            "Tree_Density": Tree_Density,
            "Trees_mgmt": Trees_mgmt,
            "Video": Video,
            "x": x,
            "y": y,
        }

        updated_dict = {}
        for k, v in updates.items():
            if v:
                db[__OBJECTID][k] = v
                updated_dict[k] = v
        return {
            "UPDATED!": updated_dict,
            "PROJECT": {__OBJECTID: db[__OBJECTID]},
        }
    else:
        return "<h1>PROJECT ID {} IS NOT FOUND!</h1>".format(__OBJECTID)


@app.route("/projects/<__OBJECTID>", methods=["DELETE"])
def delete_project(__OBJECTID):
    if __OBJECTID in db.keys():
        project_removed = db[__OBJECTID]
        del db[__OBJECTID]
        return {"PROJECT REMOVED": {__OBJECTID: project_removed}}
    else:
        return "<h1>PROJECT ID {} IS NOT FOUND!</h1>".format(__OBJECTID)


@app.route("/query-example")
def query_example():
    # if key doesn't exist, returns None
    language = request.args.get("language")

    # if key doesn't exist, returns a 400, bad request error
    framework = request.args["framework"]

    # if key doesn't exist, returns None
    website = request.args.get("website")

    return """
              <h1>The language value is: {}</h1>
              <h1>The framework value is: {}</h1>
              <h1>The website value is: {}""".format(
        language, framework, website
    )


# http://127.0.0.1:5000/query-example?language=Python&framework=Flask&website=DigitalOcean

# allow both GET and POST requests
@app.route("/form-example", methods=["GET", "POST"])
def form_example():
    # handle the POST request
    if request.method == "POST":
        language = request.form.get("language")
        framework = request.form.get("framework")
        return """
                <h1>The language value is: {}</h1>
                <h1>The framework value is: {}</h1>""".format(
            language, framework
        )

    # otherwise handle the GET request
    return """
           <form method="POST">
               <div><label>Language: <input type="text" name="language"></label></div>
               <div><label>Framework: <input type="text" name="framework"></label></div>
               <input type="submit" value="Submit">
           </form>"""


if __name__ == "__main__":
    app.run(debug=True)

# Run flask app on the cmd line
# set FLASK_APP=REST_API.py
# set FLASK_DEBUG=1
# flask run
