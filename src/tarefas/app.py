from flask import Flask, redirect, render_template, request, url_for

from tarefas.models.database import init_db
from tarefas.models.tarefa import Tarefa

app = Flask (__name__)

with app.app_context():
    init_db()

@app.route('/test')
def test():
    return 'servidor online!'

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        titulo_form = request.form['tituloTarefa'] # casa com o nome do input no form
        data_conclusao_form = request.form['dataConclusao'] #casa com o nome do input no form

        data_corrigida = data_conclusao_form or None
        # 'or' nesse caso é um operador de coalescência -> retorna o
        # primeiro valor válido

        # Instanciamos uma nova tarefa com os dados recebidos do form
        tarefa = Tarefa(titulo=titulo_form, data_conclusao=data_corrigida)

        # Salvamos a tarefa no banco
        tarefa.salvarTarefa()

        return redirect(url_for('home'))

    tarefas = Tarefa.listarTarefas()

    return render_template(
        'base.html', 
        titulo_da_pagina='Lista de tarefas do Elder',
        tarefas_da_pagina = tarefas
        )

#Crie uma nova funcionalidade para apagar cada uma das tarefas cadastradas
@app.route('/delete/<int:id>')
def apagar_id_especificado(id):
    Tarefa.apagarTarefa(id)
    return redirect(url_for('home'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    if request.method == 'POST':
        titulo_form = request.form['tituloTarefa']
        data_conclusao_form = request.form['dataConclusao']
        data_corrigida = data_conclusao_form or None

        Tarefa.atualizarTarefa(
            id_tarefa=id, 
            titulo=titulo_form, 
            data_conclusao=data_corrigida
        )

        return redirect(url_for('home'))

    tarefas = Tarefa.listarTarefas()
    # Busca usando .id_tarefa (compatível com o seu HTML)
    tarefa_selecionada = next((t for t in tarefas if t.id_tarefa == id), None)

    return render_template(
        'base.html',
        titulo_da_pagina='Editar Tarefa',
        tarefas_da_pagina=tarefas,
        tarefa_edit=tarefa_selecionada
    )




if __name__ == '__main__':
    app.run()

