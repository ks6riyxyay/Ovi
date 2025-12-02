import os
import gradio as gr
from ovi.inference import inference  # adapte conforme o seu fork do Ovi

# Diretório de saída dentro do Ovi
OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def gerar_video(prompt: str, seed: int = 42):
    """
    Função que chama o Ovi para gerar vídeo a partir de um prompt.
    Retorna o caminho do vídeo gerado.
    """
    video_path = os.path.join(OUTPUT_DIR, f"video_{seed}.mp4")
    
    # Exemplo de chamada à função de geração do Ovi
    # Adapte para a função real do seu fork
    run_inference(
        prompt=prompt,
        output_path=video_path,
        seed=seed,
        resolution="480x480",  # resolução menor para Render CPU
        duration_sec=5
    )
    return video_path

# Frontend web
iface = gr.Interface(
    fn=gerar_video,
    inputs=[gr.Textbox(label="Prompt"), gr.Slider(0, 9999, step=1, label="Seed")],
    outputs=[gr.Video(label="Vídeo gerado")],
    title="Gerador de vídeo com Ovi",
    description="Digite um prompt e gere vídeo com Ovi"
)

# Para Render.com usar a porta de ambiente
import os
port = int(os.environ.get("PORT", 8080))
iface.launch(server_name="0.0.0.0", server_port=port)
