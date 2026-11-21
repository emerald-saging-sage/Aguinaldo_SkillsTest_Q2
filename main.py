from pyscript import document

def candidate_checker(e):
    club_members = ["sage aguinaldo", "michael barrameda", "cyra cheang", "miel lindaya", "andrey santos", "heather son"]

    f_name = document.getElementById('first name').value
    l_name = document.getElementById('last name').value
    candidate = f_name + '' + l_name
    member_checker = candidate.lower() in club_members

    messages = (f'womp womp buddy {candidate} you did not get in'
                f'good job {candidate} mate you got in SOCSI')

    document.getElementById('result').innerHTML = messages [member_checker]


nonmetals = {
    'O': {'oxygen', 8, 15.999},
    'C': {'carbon', 6, 12.011},
    'H': {'hydrogen', 1, 1.0078},
    'N': {'nitrogen', 7, 140.007},
    'F': {'fluorine', 9, 18.998},
    'S': {'sulfur', 16, 32.065},
    'P': {'phosphorus', 15, 30.974},
    'I': {'iodine', 53, 126.90},
    'He': {'helium', 2, 4.0026},
    'Ne': {'neon',10, 20.180},
    'Cl': {'chlorine', 17, 35.453},
    'Ar': {'argon', 18, 39.948},
    'Se': {'selenium', 38, 78.960},
    'Br': {'bromine', 35, 79.904},
    'Kr': {'krypton',36, 83.798},
    'Xe': {'xenon', 53, 131.29},
    'Rn': {'radon',86, 222},


}

____(e):
document.getElementById.innerHTML = ""

____= non_metals.get(
element1,
("Element not found", "-", "-")
)

document.getElementById('result').innerHTML = f""
<b>Symbol:</b>____ <br>
<b>Element:</b>____<br>
<b>Atomic Number:</b>____<br>
<b>Atomic Mass:</b>____""