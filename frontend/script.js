const API_URL = 'http://localhost:8000/agendamentos';

        async function fetchAgendamentos() {
            const response = await fetch(API_URL);
            const data = await response.json();
            const lista = document.getElementById('agendamentos-list');
            lista.innerHTML = '';
            data.agendamento.forEach(agendamento => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${agendamento.data}</td>
                    <td>${agendamento.horario}</td>
                    <td>${agendamento.cliente}</td>
                    <td>${agendamento.servico}</td>
                    <td class="actions">
                        <button class="edit-btn" onclick="editAgendamento('${agendamento.id}')">Editar</button>
                        <button class="delete-btn" onclick="deleteAgendamento('${agendamento.id}')">Excluir</button>
                    </td>
                `;
                lista.appendChild(row);
            });
        }

        async function createOrUpdateAgendamento(event) {
            event.preventDefault();
            const id = document.getElementById('agendamento-id').value;
            const agendamento = {
                data: document.getElementById('data').value,
                horario: document.getElementById('horario').value,
                cliente: document.getElementById('cliente').value,
                servico: document.getElementById('servico').value
            };
            
            const method = id ? 'PUT' : 'POST';
            const url = id ? `${API_URL}/${id}` : API_URL;
            await fetch(url, {
                method,
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(agendamento)
            });
            document.getElementById('agendamento-form').reset();
            fetchAgendamentos();
        }

        async function editAgendamento(id) {
            const response = await fetch(`${API_URL}/${id}`);
            const agendamento = await response.json();
            document.getElementById('agendamento-id').value = agendamento.id;
            document.getElementById('data').value = agendamento.data;
            document.getElementById('horario').value = agendamento.horario;
            document.getElementById('cliente').value = agendamento.cliente;
            document.getElementById('servico').value = agendamento.servico;
        }

        async function deleteAgendamento(id) {
            if (confirm('Tem certeza que deseja excluir este agendamento?')) {
                await fetch(`${API_URL}/${id}`, { method: 'DELETE' });
                fetchAgendamentos();
            }
        }

        document.getElementById('agendamento-form').addEventListener('submit', createOrUpdateAgendamento);

        fetchAgendamentos();