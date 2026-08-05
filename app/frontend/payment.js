const pass = JSON.parse(localStorage.getItem("busPassData"));

if (pass) {

    document.getElementById("student").innerText = pass.student_id;

    document.getElementById("passType").innerText = pass.pass_type;

    document.getElementById("route").innerText =
        pass.source + " → " + pass.destination;

    let amount = 300;

    if (pass.pass_type === "Monthly") {
        amount = 300;
    } else if (pass.pass_type === "Quarterly") {
        amount = 800;
    } else if (pass.pass_type === "Yearly") {
        amount = 3000;
    }

    document.getElementById("amount").innerText = amount;
}

function payNow() {

    alert("✅ Payment Successful!");

    window.location.href = "receipt.html";
}