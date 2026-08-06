const API = "http://127.0.0.1:8000";

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
        console.error(error);
        alert("Server Error");
    }

}

async function loginStudent() {

    const data = {
        email: document.getElementById("email").value,
        password: document.getElementById("password").value
    };


console.log(data.email);

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

    // Student information save
    localStorage.setItem("studentEmail", data.email);

    // पुढच्या page वर जा
    window.location.href = "apply.html";

} else {

    alert(result.detail || "Invalid Email or Password");

}

    } catch (error) {
        console.error(error);
        alert("Server Error");
    }
}

async function applyBusPass() {

    const studentIdRaw = document.getElementById("student_id").value;
    const studentId = parseInt(studentIdRaw);
    if (isNaN(studentId)) {
        alert("Please enter a valid Student ID");
        return;
    }

    const data = {
        student_id: studentId,
        source: document.getElementById("source").value,
        destination: document.getElementById("destination").value,
        pass_type: document.getElementById("pass_type").value,
        start_date: document.getElementById("start_date").value,
        end_date: document.getElementById("end_date").value
    };

    try {

        const response = await fetch(`${API}/buspass/apply`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

if (response.ok) {

    
    localStorage.setItem("busPassData", JSON.stringify(data));

    alert("✅ Bus Pass Applied Successfully");

    
    window.location.href = "payment.html";

} else {

    alert(result.detail || "Failed to Apply");

}
} catch (error) {
    console.error(error);
    alert("Server Error");
}
}



async function checkStatus() {

    const studentId = document.getElementById("student_id").value;

    try {

        const response = await fetch(`${API}/buspass/student/${studentId}`);
        const json = await response.json().catch(() => null);

        if (response.ok) {

            if (!json || json.length === 0) {
                document.getElementById("result").innerHTML = `<p style="color:orange;">No bus pass found for this student.</p>`;
                return;
            }

            const pass = json[json.length - 1];

            document.getElementById("result").innerHTML = `
                <h3>Bus Pass Details</h3>
                <p><b>Source:</b> ${pass.source}</p>
                <p><b>Destination:</b> ${pass.destination}</p>
                <p><b>Pass Type:</b> ${pass.pass_type}</p>
                <p><b>Start Date:</b> ${pass.start_date}</p>
                <p><b>End Date:</b> ${pass.end_date}</p>
                <p><b>Status:</b> ${pass.status}</p>
            `;

        } else {

            document.getElementById("result").innerHTML =
                `<p style="color:red;">${data.detail}</p>`;

        }

    } catch (error) {
        console.error(error);
        alert("Server Error");
    }
}





async function loadBusPasses() {

    try {

        const response = await fetch(`${API}/admin/buspasses`);
        const data = await response.json();

        const tbody = document.querySelector("#passTable tbody");
        if (!tbody) return;
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
                    <button class="btn btn-success btn-sm"
                        onclick="updateStatus(${pass.id}, 'Approved')">
                        Approve
                    </button>

                    <button class="btn btn-danger btn-sm"
                        onclick="updateStatus(${pass.id}, 'Rejected')">
                        Reject
                    </button>
                </td>

            </tr>
            `;

        });

    } catch (error) {
        console.error(error);
    }
}





async function updateStatus(passId, status) {

    try {

        const response = await fetch(
            `${API}/admin/buspass/${passId}?status=${encodeURIComponent(status)}`,
            {
                method: "PUT"
            }
        );

        const result = await response.json().catch(() => null);

        if (response.ok) {
            alert("✅ Status Updated");
            loadBusPasses();
        } else {
            alert(result.detail || "Update Failed");
        }

    } catch (error) {
        console.error(error);
        alert("Server Error");
    }

}




function logout() {

    localStorage.removeItem("studentEmail");

    alert("✅ Logout Successful");  
  
    window.location.href = "login.html";
}


function adminLogout() {

    alert("✅ Admin Logout Successful");

    window.location.href = "login.html";
}








