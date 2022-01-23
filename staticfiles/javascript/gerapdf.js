 gerarPDF() {
      let doc = window.open("", "", "width=800, height=600");
      let html =
        `
      <html><head><title>Gráficos documentados - ` +
        JSON.stringify() +
        ` </title></head>
        <body style="font-family: 'Roboto', sans-serif;display: flex; flex-direction: row; justify-content: space-between">
          <div style="margin-top: 60px">
            <div style="border: 1px solid #c22a1f; border-radius: 10px;">
              <div style="background-color: #c22a1f;color: #fff;padding: 5px;border-top-left-radius: 10px;border-top-right-radius: 10px;">
                <h3>Satisfação total dos alunos:</h3>
              </div>
              <div style="padding: 10px;">
                <p>` +
                 </tr>
              </tbody>
            </table>
          </div>
        </body>
      </html>
      `;
      doc.document.write(html);
      doc.document.close();
      doc.print();