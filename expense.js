const splitType = document.getElementById("split-type");
function toggleFields() {
    if (splitType.value === "friend") {
        friendOwes.style.display = "block";
        friendName.style.display = "block";
        groupFields.style.display = "none";
        groupCost.style.display = "none";
        groupName.style.display = "none";

    } else if (splitType.value === "group") {
        friendOwes.style.display = "none";
        friendName.style.display = "none";
        groupFields.style.display = "block";
        groupCost.style.display = "block";
        groupName.style.display = "block";
    }
}

const friendOwes = document.getElementById("friend-owes");
const friendName = document.getElementById("friend-name");
const groupFields = document.getElementById("group-fields");
const groupCost = document.getElementById("group-cost");
const groupMem = document.getElementById("group-size");
const groupName = document.getElementById("group-name");

const totAmount = document.getElementById("amount");
const userAmount = document.getElementById("amount_u");


splitType.addEventListener("change", toggleFields);
totAmount.addEventListener("input", Calculateamount);
userAmount.addEventListener("input", Calculateamount);

function Calculateamount() {
    const tot_amount = totAmount.value;
    const user_amount = userAmount.value;
    const owed_amount = user_amount - (tot_amount) / 2;
    var amount_owed = document.getElementById("friend-cost-per-person");
    amount_owed.innerHTML = `<p>${owed_amount}</p>`;
}

splitType.addEventListener("change", toggleFields);
totAmount.addEventListener("input", CalculateGroupAmount);
userAmount.addEventListener("input", CalculateGroupAmount);


function CalculateGroupAmount() {
    const tot_amount = totAmount.value;
    const user_amount = userAmount.value;
    const members = groupMem.value;
    const owed_amount2 = ((user_amount - (tot_amount) / members) / members);
    var amount_owed = document.getElementById("group-cost-per-person");
    amount_owed.innerHTML = `<p>${owed_amount2}</p>`;
}
