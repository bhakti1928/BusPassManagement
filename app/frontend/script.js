const API = "https://buspassmanagement-vqpu.onrender.com";


// ===============================
// STUDENT REGISTER
// ===============================

async function registerStudent() {

    const data = {
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        mobile: document.getElementById("mobile").value,
        college: document.getElementById("college").value,
        password: document.getElementById("password").value
    };

    try {

        const response = await fetch(`${API}/student/register`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (response.ok) {

            alert("✅ Student Registered Successfully");

            window.location.href = "login.html";

        } else {

            alert(result.detail || "Registration Failed");

        }

    } catch (error) {

        console.error("Registration Error:", error);

        alert("Server Error");

    }
}


// ===============================
// STUDENT LOGIN
// ===============================

async function loginStudent() {

    const data = {
        email: document.getElementById("email").value,
        password: document.getElementById("password").value
    };

    try {

        const response = await fetch(`${API}/student/login`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (response.ok) {

            alert("✅ Login Successful");

            // Save logged-in student information
            localStorage.setItem("studentEmail", data.email);
            localStorage.setItem("studentId", result.student.id);

            // Go to Apply Pass page
            window.location.href = "apply.html";

        } else {

            alert(result.detail || "Invalid Email or Password");

        }

    } catch (error) {

        console.error("Login Error:", error);

        alert("Server Error");

    }
}


// ===============================
// APPLY BUS PASS
// ===============================

async function applyBusPass() {

    const studentId =
        document.getElementById("student_id").value;

    if (!studentId) {

        alert("Student ID not found. Please login again.");

        window.location.href = "login.html";

        return;
    }


    const data = {

        student_id: parseInt(studentId),

        source:
            document.getElementById("source").value,

        destination:
            document.getElementById("destination").value,

        pass_type:
            document.getElementById("pass_type").value,

        start_date:
            document.getElementById("start_date").value,

        end_date:
            document.getElementById("end_date").value
    };


    try {

        const response = await fetch(
            `${API}/buspass/apply`,
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(data)
            }
        );


        const result = await response.json();


        if (response.ok) {

            localStorage.setItem(
                "busPassData",
                JSON.stringify(result)
            );

            alert("✅ Bus Pass Applied Successfully");

            window.location.href = "payment.html";

        } else {

            alert(
                result.detail ||
                "Failed to Apply Bus Pass"
            );

        }

    } catch (error) {

        console.error("Bus Pass Error:", error);

        alert("Server Error. Please try again.");

    }
}


// ===============================
// CHECK BUS PASS STATUS
// ===============================

async function checkStatus() {

    const studentId =
        document.getElementById("student_id").value;


    if (!studentId) {

        alert("Student ID not found.");

        return;
    }


    try {

        const response = await fetch(
            `${API}/buspass/student/${studentId}`
        );


        const data = await response.json();


        if (response.ok) {

            if (!data || data.length === 0) {

                document.getElementById("result").innerHTML =
                    `<p style="color:red;">
                        No bus pass found.
                    </p>`;

                return;
            }


            const pass = data[data.length - 1];


            document.getElementById("result").innerHTML = `

                <h3>Bus Pass Details</h3>

                <p>
                    <b>Source:</b>
                    ${pass.source}
                </p>

                <p>
                    <b>Destination:</b>
                    ${pass.destination}
                </p>

                <p>
                    <b>Pass Type:</b>
                    ${pass.pass_type}
                </p>

                <p>
                    <b>Start Date:</b>
                    ${pass.start_date}
                </p>

                <p>
                    <b>End Date:</b>
                    ${pass.end_date}
                </p>

                <p>
                    <b>Status:</b>
                    ${pass.status}
                </p>

            `;

        } else {

            document.getElementById("result").innerHTML =

                `<p style="color:red;">
                    ${data.detail || "Unable to get status"}
                </p>`;

        }

    } catch (error) {

        console.error("Status Error:", error);

        alert("Server Error");

    }
}


// ===============================
// ADMIN - LOAD BUS PASSES
// ===============================

async function loadBusPasses() {

    try {

        const response =
            await fetch(`${API}/admin/buspasses`);


        const data = await response.json();


        const tbody =
            document.querySelector("#passTable tbody");


        tbody.innerHTML = "";


        data.forEach(pass => {

            tbody.innerHTML += `

                <tr>

                    <td>${pass.id}</td>

                    <td>${pass.student_id}</td>

                    <td>${pass.source}</td>

                    <td>${pass.destination}</td>

                    <td>${pass.pass_type}</td>

                    <td>

                        <span class="badge ${
                            pass.status === "Approved"
                                ? "bg-success"
                                : pass.status === "Rejected"
                                ? "bg-danger"
                                : "bg-warning text-dark"
                        }">

                            ${pass.status}

                        </span>

                    </td>


                    <td>

                        <button
                            class="btn btn-success btn-sm"
                            onclick="updateStatus(
                                ${pass.id},
                                'Approved'
                            )"
                        >
                            Approve
                        </button>


                        <button
                            class="btn btn-danger btn-sm"
                            onclick="updateStatus(
                                ${pass.id},
                                'Rejected'
                            )"
                        >
                            Reject
                        </button>

                    </td>

                </tr>

            `;

        });

    } catch (error) {

        console.error("Admin Error:", error);

    }
}


// ===============================
// ADMIN - UPDATE STATUS
// ===============================

async function updateStatus(passId, status) {

    try {

        const response = await fetch(
            `${API}/admin/buspass/${passId}?status=${status}`,
            {
                method: "PUT"
            }
        );


        const result = await response.json();


        if (response.ok) {

            alert("✅ Status Updated");

            loadBusPasses();

        } else {

            alert(
                result.detail ||
                "Update Failed"
            );

        }

    } catch (error) {

        console.error("Update Status Error:", error);

        alert("Server Error");

    }
}


// ===============================
// STUDENT LOGOUT
// ===============================

function logout() {

    localStorage.removeItem("studentEmail");

    localStorage.removeItem("studentId");

    localStorage.removeItem("busPassData");


    alert("✅ Logout Successful");


    window.location.href = "login.html";
}


// ===============================
// ADMIN LOGOUT
// ===============================

function adminLogout() {

    alert("✅ Admin Logout Successful");

    window.location.href = "login.html";
}