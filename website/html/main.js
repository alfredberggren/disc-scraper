// fetches discs

fetch("http://127.0.0.1:8000/data.json")
  .then((response) => response.json())
  .then((data) => {
    const tableBody = document.getElementById("disc-table-body");
    data.data.forEach((item) => {
      const tableRow = document.createElement("tr");
      tableRow.innerHTML = `
        <td>${item.mold_name}</td>
        <td>${item.plastic}</td>
        <td>${item.manufacturer}</td>
        <td>${item.price}</td>
        `;
      tableBody.appendChild(tableRow);
    });
  })
  .catch((error) => console.error("Error: ", error));
