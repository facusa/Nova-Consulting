import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

repo_html = """
        <!-- Acceso a Clientes -->
        <section id="repo-acceso" class="section" style="padding: 40px 0; text-align: center;">
            <div class="container">
                <button id="btn-login-repo" class="btn-linkedin" style="background-color: var(--text-main); border: none; font-size: 13px; padding: 6px 12px; margin-top: -20px; box-shadow: none;">Acceso a Clientes</button>
            </div>
        </section>

        <!-- Repositorio de Entregables Oculto -->
        <section id="entregables" class="section" style="display: none;">
            <div class="container">
                <div class="section-header">
                    <h2 class="section-title">Repositorio de Entregables</h2>
                    <div class="section-line"></div>
                    <p class="section-subtitle">Toda la documentación generada durante la consultoría, disponible para descarga exclusiva.</p>
                </div>
                <div class="deliverables-container glass-panel">
                    <div class="table-responsive">
                        <table class="deliverables-table">
                            <thead>
                                <tr>
                                    <th>Documento</th>
                                    <th>Formato</th>
                                    <th>Descripción</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr onclick="window.open('https://canva.link/vynqmja8yzmeb6v', '_blank')" style="cursor: pointer;" class="clickable-row">
                                    <td>
                                        <div class="doc-name">
                                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="doc-icon">
                                                <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                                                <line x1="3" y1="9" x2="21" y2="9"></line>
                                            </svg>
                                            Presentación de Canva
                                        </div>
                                    </td>
                                    <td><span class="tag tag-slide">PPT</span></td>
                                    <td>Presentación visual del proyecto en Canva.</td>
                                </tr>
                                <tr onclick="window.open('https://economicasuba-my.sharepoint.com/:v:/g/personal/96lc30494821_campus_economicas_uba_ar/IQCBsmIHjxAiS7vRA5AShQcqAaXbI-vC0opppEdGtcVSysk?e=oMGkVr&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D', '_blank')" style="cursor: pointer;" class="clickable-row">
                                    <td>
                                        <div class="doc-name">
                                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="doc-icon">
                                                <polygon points="23 7 16 12 23 17 23 7"></polygon>
                                                <rect x="1" y="5" width="15" height="14" rx="2" ry="2"></rect>
                                            </svg>
                                            Elevator Pitch
                                        </div>
                                    </td>
                                    <td><span class="tag tag-video">MOV</span></td>
                                    <td>Video resumen de presentación del proyecto.</td>
                                </tr>
                                <tr onclick="window.open('entregas/01 Selección del Caso CORREGIDO.docx', '_blank')" style="cursor: pointer;" class="clickable-row">
                                    <td>
                                        <div class="doc-name">
                                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="doc-icon">
                                                <path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z" />
                                                <polyline points="14 2 14 8 20 8" />
                                            </svg>
                                            01 Selección del Caso
                                        </div>
                                    </td>
                                    <td><span class="tag tag-doc">DOCX</span></td>
                                    <td>Justificación y elección del caso de estudio de Full Basics.</td>
                                </tr>
                                <tr onclick="window.open('entregas/02 Diagnostico organizacional - CORREGIDO.docx', '_blank')" style="cursor: pointer;" class="clickable-row">
                                    <td>
                                        <div class="doc-name">
                                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="doc-icon">
                                                <path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z" />
                                                <polyline points="14 2 14 8 20 8" />
                                            </svg>
                                            02 Diagnóstico Organizacional
                                        </div>
                                    </td>
                                    <td><span class="tag tag-doc">DOCX</span></td>
                                    <td>Análisis de la situación actual y modelo operativo.</td>
                                </tr>
                                <tr onclick="window.open('entregas/03 Arquitectura Empresarial Origen - CORREGIDO.docx', '_blank')" style="cursor: pointer;" class="clickable-row">
                                    <td>
                                        <div class="doc-name">
                                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="doc-icon">
                                                <path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z" />
                                                <polyline points="14 2 14 8 20 8" />
                                            </svg>
                                            03 Arquitectura Empresarial Origen
                                        </div>
                                    </td>
                                    <td><span class="tag tag-doc">DOCX</span></td>
                                    <td>Descripción detallada de la arquitectura AS-IS.</td>
                                </tr>
                                <tr onclick="window.open('entregas/04 Innovación para la transformación - CORREGIDO.docx', '_blank')" style="cursor: pointer;" class="clickable-row">
                                    <td>
                                        <div class="doc-name">
                                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="doc-icon">
                                                <path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z" />
                                                <polyline points="14 2 14 8 20 8" />
                                            </svg>
                                            04 Innovación para la Transformación
                                        </div>
                                    </td>
                                    <td><span class="tag tag-doc">DOCX</span></td>
                                    <td>Propuestas de innovación aplicadas al modelo de negocio.</td>
                                </tr>
                                <tr onclick="window.open('entregas/05 Arquitectura Empresarial Destino - TERMINADO.docx', '_blank')" style="cursor: pointer;" class="clickable-row">
                                    <td>
                                        <div class="doc-name">
                                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="doc-icon">
                                                <path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z" />
                                                <polyline points="14 2 14 8 20 8" />
                                            </svg>
                                            05 Arquitectura Empresarial Destino
                                        </div>
                                    </td>
                                    <td><span class="tag tag-doc">DOCX</span></td>
                                    <td>Diseño de la arquitectura TO-BE esperada.</td>
                                </tr>
                                <tr onclick="window.open('entregas/06 Matriz de brechas y escenarios.docx', '_blank')" style="cursor: pointer;" class="clickable-row">
                                    <td>
                                        <div class="doc-name">
                                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="doc-icon">
                                                <path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z" />
                                                <polyline points="14 2 14 8 20 8" />
                                            </svg>
                                            06 Matriz de Brechas y Escenarios
                                        </div>
                                    </td>
                                    <td><span class="tag tag-doc">DOCX</span></td>
                                    <td>Análisis comparativo y evaluación de escenarios.</td>
                                </tr>
                                <tr onclick="window.open('entregas/07 Alcance del proyecto - CORREGIDO.docx', '_blank')" style="cursor: pointer;" class="clickable-row">
                                    <td>
                                        <div class="doc-name">
                                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="doc-icon">
                                                <path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z" />
                                                <polyline points="14 2 14 8 20 8" />
                                            </svg>
                                            07 Alcance del Proyecto
                                        </div>
                                    </td>
                                    <td><span class="tag tag-doc">DOCX</span></td>
                                    <td>Definición de límites, objetivos y requerimientos.</td>
                                </tr>
                                <tr onclick="window.open('entregas/08 Análisis del mercado y benchmarking - CORREGIDO.docx', '_blank')" style="cursor: pointer;" class="clickable-row">
                                    <td>
                                        <div class="doc-name">
                                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="doc-icon">
                                                <path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z" />
                                                <polyline points="14 2 14 8 20 8" />
                                            </svg>
                                            08 Análisis del Mercado
                                        </div>
                                    </td>
                                    <td><span class="tag tag-doc">DOCX</span></td>
                                    <td>Investigación de soluciones y proveedores (RFI/RFP).</td>
                                </tr>
                                <tr onclick="window.open('entregas/09 Factibilidad.docx', '_blank')" style="cursor: pointer;" class="clickable-row">
                                    <td>
                                        <div class="doc-name">
                                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="doc-icon">
                                                <path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z" />
                                                <polyline points="14 2 14 8 20 8" />
                                            </svg>
                                            09 Factibilidad
                                        </div>
                                    </td>
                                    <td><span class="tag tag-doc">DOCX</span></td>
                                    <td>Análisis de viabilidad técnica, operativa y económica.</td>
                                </tr>
                                <tr onclick="window.open('entregas/09 RFP.xlsx', '_blank')" style="cursor: pointer;" class="clickable-row">
                                    <td>
                                        <div class="doc-name">
                                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="doc-icon">
                                                <path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z" />
                                                <polyline points="14 2 14 8 20 8" />
                                            </svg>
                                            09 RFP (Excel)
                                        </div>
                                    </td>
                                    <td><span class="tag tag-sheet">XLSX</span></td>
                                    <td>Planilla de requerimientos y evaluación para proveedores.</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </section>

        <!-- Login Modal -->
        <div id="login-modal" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 1000; justify-content: center; align-items: center; backdrop-filter: blur(5px);">
            <div class="glass-panel" style="width: 100%; max-width: 350px; padding: 40px 32px; background: white; border-radius: 16px; position: relative; text-align: center; box-shadow: 0 20px 40px rgba(0,0,0,0.2);">
                <span id="close-modal" style="position: absolute; right: 20px; top: 15px; font-size: 24px; cursor: pointer; color: #666;">&times;</span>
                <h3 style="margin-bottom: 8px; color: var(--text-main);">Acceso Restringido</h3>
                <p style="font-size: 14px; color: var(--text-muted); margin-bottom: 24px;">Ingrese sus credenciales para acceder al repositorio.</p>
                <input type="text" id="repo-user" placeholder="Usuario" style="width: 100%; padding: 12px; margin-bottom: 16px; border: 1px solid #e2e8f0; border-radius: 8px; outline: none; font-family: inherit; box-sizing: border-box;">
                <input type="password" id="repo-pass" placeholder="Contraseña" style="width: 100%; padding: 12px; margin-bottom: 24px; border: 1px solid #e2e8f0; border-radius: 8px; outline: none; font-family: inherit; box-sizing: border-box;">
                <button id="btn-submit-login" class="btn-linkedin" style="width: 100%; justify-content: center;">Ingresar</button>
                <p id="login-error" style="color: #ef4444; font-size: 13px; margin-top: 16px; display: none; font-weight: 500;">Credenciales incorrectas.</p>
            </div>
        </div>
"""

# Insert right before </main>
content = content.replace("    </main>", repo_html + "\n    </main>")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html")
