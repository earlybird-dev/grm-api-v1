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
            <h1>Welcome to Global Restoration Monitor API 1.1</h1>
            <h2>API Documentation: <a href="https://grm-api-testing.stoplight.io/docs/grm-api-v1-0/">https://grm-api-testing.stoplight.io/docs/grm-api-v1-0/</h2>
            """


@app.route("/projects", methods=["GET"])
def get_project():
    Project_ID = request.args.get("id")
    if Project_ID:
        if Project_ID in db.keys():
            return db[Project_ID]
        else:
            return "<h1>PROJECT ID {} IS NOT FOUND!</h1>".format(Project_ID)

    return {"PROJECTS": db}


@app.route("/projects/add", methods=["GET", "POST"])
def add_project():

    # Handle the POST request
    if request.method == "POST":
        Project_ID = request.form.get("Project_ID")
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

        if Project_ID:
            if Project_ID in db.keys():
                return "<h1>PROJECT ID {} EXISTS!</h1>".format(Project_ID)
            else:
                new_project = {
                    "Project_ID": Project_ID,
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

                db[Project_ID] = new_project
                return {"NEW PROJECT CREATED!": {Project_ID: new_project}}
        else:
            return "<h1>Project_ID IS REQUIRED!</h1>"

    # Otherwise handle the GET request
    return """
           <form method="POST">
               <div><label>Project_ID (*): <input type="text" name="Project_ID"></label></div>
               <div><label>Budget: <input type="text" name="Budget"></label></div>
               <div><label>C02e_To_Date: <input type="text" name="C02e_To_Date"></label></div>
               <div><label>Description: <input type="text" name="Description"></label></div>
               <div><label>DirectBeneficiaries_HH: <input type="text" name="DirectBeneficiaries_HH"></label></div>
               <div><label>District: <input type="text" name="District"></label></div>
               <div><label>Donor_Principal: <input type="text" name="Donor_Principal"></label></div>
               <div><label>Donors_Other: <input type="text" name="Donors_Other"></label></div>
               <div><label>End_Year: <input type="text" name="End_Year"></label></div>
               <div><label>Implementing_Partners: <input type="text" name="Implementing_Partners"></label></div>
               <div><label>InDirectBeneficiaries_HH: <input type="text" name="InDirectBeneficiaries_HH"></label></div>
               <div><label>Land_Area: <input type="text" name="Land_Area"></label></div>
               <div><label>Logo: <input type="text" name="Logo"></label></div>
               <div><label>Men_Trained: <input type="text" name="Men_Trained"></label></div>
               <div><label>Organisation: <input type="text" name="Organisation"></label></div>
               <div><label>People_Trained: <input type="text" name="People_Trained"></label></div>
               <div><label>Practice: <input type="text" name="Practice"></label></div>
               <div><label>Proj_Code: <input type="text" name="Proj_Code"></label></div>
               <div><label>Proj_Currency: <input type="text" name="Proj_Currency"></label></div>
               <div><label>Proj_Status: <input type="text" name="Proj_Status"></label></div>
               <div><label>Project_Description: <input type="text" name="Project_Description"></label></div>
               <div><label>Project_Value: <input type="text" name="Project_Value"></label></div>
               <div><label>Site_Code: <input type="text" name="Site_Code"></label></div>
               <div><label>Start_Year: <input type="text" name="Start_Year"></label></div>
               <div><label>Tree_Density: <input type="text" name="Tree_Density"></label></div>
               <div><label>Trees_mgmt: <input type="text" name="Trees_mgmt"></label></div>
               <div><label>x: <input type="text" name="x"></label></div>
               <div><label>y: <input type="text" name="y"></label></div>
               <input type="submit" value="Submit">
           </form>"""


@app.route("/projects/<Project_ID>", methods=["PUT"])
def update_project(Project_ID):
    if Project_ID in db.keys():
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
                db[Project_ID][k] = v
                updated_dict[k] = v
        return {
            "UPDATED!": updated_dict,
            "PROJECT": {Project_ID: db[Project_ID]},
        }
    else:
        return "<h1>PROJECT ID {} IS NOT FOUND!</h1>".format(Project_ID)


@app.route("/projects/<Project_ID>", methods=["DELETE"])
def delete_project(Project_ID):
    if Project_ID in db.keys():
        project_removed = db[Project_ID]
        del db[Project_ID]
        return {"PROJECT REMOVED": {Project_ID: project_removed}}
    else:
        return "<h1>PROJECT ID {} IS NOT FOUND!</h1>".format(Project_ID)


@app.route("/projects/query")
def query_example():
    # If key doesn't exist, returns None
    Nation = request.args.get("Nation")
    Organisation = request.args.get("Organisation")
    Donor_Principal = request.args.get("Donor_Principal")

    output_1 = db.copy()
    if Nation is not None:
        for k, v in db.items():
            if v["Nation"] != Nation:
                del output_1[k]
    output_2 = output_1.copy()
    if Organisation is not None:
        for k, v in output_1.items():
            if v["Organisation"] != Organisation:
                del output_2[k]
    output_3 = output_2.copy()
    if Donor_Principal is not None:
        for k, v in output_2.items():
            if v["Donor_Principal"] != Donor_Principal:
                del output_3[k]

    return {"Project List": list(output_3.keys())}


# http://127.0.0.1:5000/query?Nation=Ethiopia&Organisation=...&Donor_Principal=...

if __name__ == "__main__":
    app.run(debug=True)

# Run flask app on the cmd line
# set FLASK_APP=main.py
# set FLASK_DEBUG=1
# flask run
