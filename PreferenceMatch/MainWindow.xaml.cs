using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace Gale_Shapley {
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window {
        public static bool continuar = false;
        class Grafo {
            private static Grafo grafo = new Grafo();
            public List<Vertice> hombres = new List<Vertice>(), mujeres = new List<Vertice>();
            private List<List<Vertice>> casados = new List<List<Vertice>>();
            private Canvas canvasPanel;
            public void EnviarSolicitudes() {
                if (hombres.Count > 0 && mujeres.Count > 0) {
                    foreach (Vertice hombre in hombres) {
                        hombre.EnviarSolicitud(hombre);
                    }
                    foreach (Vertice mujer in mujeres) {
                        mujer.RevisarPretendientes();
                    }
                    foreach (List<Vertice> pareja in casados) {
                        if (hombres.Contains(pareja[0])) {
                            hombres.Remove(pareja[0]);
                        }
                        if (mujeres.Contains(pareja[1])) {
                            mujeres.Remove(pareja[1]);
                        }
                    }
                    //EnviarSolicitudes();
                }
                else {
                    foreach (List<Vertice> pareja in casados) {
                        Console.WriteLine(pareja[0].nombre + "," + pareja[1].nombre);
                    }
                    return;
                }
            }
            public void Aceptacion(List<Vertice> recienCasados) {
                casados.Add(recienCasados);
                //hombres.Remove(recienCasados[0]);
                //mujeres.Remove(recienCasados[1]);
            }
            public static Grafo GetGrafo() {
                return grafo;
            }

            public void DibujarVertices() {
                // Create a Canvas Panel control    
                Canvas canvasPanel = new Canvas {
                    // Set Canvas Panel properties    
                    Background = new SolidColorBrush(Colors.White),
                    Width = 400,
                    Height = 400
                };
                Button button = new Button();
                button.Content = "Siguiente \n paso";
                button.Click += new RoutedEventHandler(Button_Click);
                canvasPanel.Children.Add(button);
                Application.Current.MainWindow.Content = canvasPanel;

                SolidColorBrush verticeColor = new SolidColorBrush(Colors.Red);
                SolidColorBrush verticeColorMujer = new SolidColorBrush(Colors.Blue);
                for (int i = 0; i < hombres.Count; i++) {
                    Ellipse newEllipse = new Ellipse {
                        Fill = verticeColor,
                        StrokeThickness = 2,
                        Stroke = Brushes.Black,
                        Width = (canvasPanel.Width / 2) / hombres.Count,
                        Height = (canvasPanel.Width / 2) / hombres.Count
                    };
                    canvasPanel.Children.Add(newEllipse);
                    Canvas.SetLeft(newEllipse, newEllipse.Width + ((canvasPanel.Width / 2) / hombres.Count) * 1.5 * i);
                    Canvas.SetTop(newEllipse, newEllipse.Height / 2);
                    hombres[i].AgregarGraficoVertice(newEllipse);
                }

                for (int i = 0; i < mujeres.Count; i++) {
                    Ellipse newEllipse = new Ellipse {
                        Fill = verticeColorMujer,
                        StrokeThickness = 2,
                        Stroke = Brushes.Black,
                        Width = (canvasPanel.Width / 2) / mujeres.Count,
                        Height = (canvasPanel.Width / 2) / mujeres.Count
                    };
                    canvasPanel.Children.Add(newEllipse);
                    List<double> coordinates = new List<double>();
                    Canvas.SetTop(newEllipse, canvasPanel.Height - newEllipse.Height);
                    Canvas.SetLeft(newEllipse, newEllipse.Width + ((canvasPanel.Width / 2) / mujeres.Count) * 1.5 * i);
                    mujeres[i].AgregarGraficoVertice(newEllipse);

                }

                foreach (Vertice hombre in hombres) {
                    hombre.AgregarGraficoArista(canvasPanel);
                }
            }

            private void Button_Click(object sender, EventArgs e) {
                EnviarSolicitudes();
            }
        }
        class Vertice {
            public string nombre { private set; get; }
            List<Vertice> preferencia = new List<Vertice>();
            List<Vertice> invitaciones = new List<Vertice>();
            public Ellipse graficoVertice;
            List<Line> aristas = new List<Line>();
            Canvas canvasPanel;
            public void AgregarGraficoVertice(Ellipse uIElement) {
                graficoVertice = uIElement;
            }
            public void AgregarGraficoArista(Canvas canvasPanel) {
                this.canvasPanel = canvasPanel;
                for (int i = 0; i < preferencia.Count; i++) {

                    Line myLine = new Line();
                    //myLine.Stroke = System.Windows.Media.Brushes.White;
                    myLine.Stroke = System.Windows.Media.Brushes.LightGray;


                    Point origen = new Point(Canvas.GetLeft(graficoVertice), Canvas.GetTop(graficoVertice));
                    myLine.X1 = graficoVertice.TransformToAncestor(canvasPanel).Transform(origen).X + graficoVertice.Width / 2;
                    myLine.Y1 = graficoVertice.TransformToAncestor(canvasPanel).Transform(origen).Y +
                        graficoVertice.Height;

                    Point destino = new Point(Canvas.GetLeft(preferencia[i].graficoVertice), Canvas.GetTop(preferencia[i].graficoVertice));
                    myLine.X2 = graficoVertice.TransformToAncestor(canvasPanel).Transform(destino).X + preferencia[0].graficoVertice.Width / 2;
                    myLine.Y2 = graficoVertice.TransformToAncestor(canvasPanel).Transform(destino).Y;

                    myLine.StrokeThickness = 5;
                    canvasPanel.Children.Add(myLine);
                    aristas.Add(myLine);
                }
            }
            public Vertice(String nuevoNombre) {
                nombre = nuevoNombre;
            }
            public void AgregarPreferencia(List<Vertice> preferidas) {
                preferencia = preferidas;
            }
            public void EnviarSolicitud(Vertice pretendiente) {
                if (preferencia.Count > 0) {
                    preferencia[0].RecibirSolicitud(pretendiente);
                    aristas[0].Stroke = System.Windows.Media.Brushes.Blue;
                }
            }
            public void RecibirSolicitud(Vertice pretendiente) {
                if (!invitaciones.Contains(pretendiente)) {
                    invitaciones.Add(pretendiente);
                }
            }
            public void Aceptar(bool aceptado) {
                if (aceptado) {
                    List<Vertice> esposos = new List<Vertice> {
                        this,
                        preferencia[0]
                    };
                    Grafo.GetGrafo().Aceptacion(esposos);
                    aristas[0].Stroke = System.Windows.Media.Brushes.Red;
                }
                else {
                    preferencia.RemoveAt(0);
                    aristas[0].Stroke = System.Windows.Media.Brushes.Black;
                    aristas.RemoveAt(0);
                }

            }
            public void RevisarPretendientes() {
                int indice = 1000;
                foreach (Vertice hombre in invitaciones) {
                    int indPRef = preferencia.IndexOf(hombre);
                    indice = indPRef < indice ? indPRef : indice;
                }
                foreach (Vertice hombre in invitaciones) {
                    if (hombre == preferencia[indice]) {
                        hombre.Aceptar(true);
                    }
                    else {
                        hombre.Aceptar(false);
                    }
                }
            }
        }

        public MainWindow() {
            InitializeComponent();
            Vertice jose = new Vertice("Jose");
            Vertice pepe = new Vertice("Pepe");
            Vertice johor = new Vertice("Johor");

            Vertice david = new Vertice("David");
            Vertice loui = new Vertice("Loui");
            Vertice roman = new Vertice("Roman");

            jose.AgregarPreferencia(new List<Vertice> { roman, david, loui });
            pepe.AgregarPreferencia(new List<Vertice> { roman, loui, david });
            johor.AgregarPreferencia(new List<Vertice> { roman, david, loui });

            david.AgregarPreferencia(new List<Vertice> { jose, johor, pepe });
            loui.AgregarPreferencia(new List<Vertice> { pepe, jose, johor });
            roman.AgregarPreferencia(new List<Vertice> { pepe, jose, johor });

            Grafo.GetGrafo().hombres = new List<Vertice> { jose, pepe, johor };
            Grafo.GetGrafo().mujeres = new List<Vertice> { loui, david, roman };

            Grafo.GetGrafo().DibujarVertices();

            //Grafo.GetGrafo().EnviarSolicitudes();
        }

        private void Button_Click(object sender, RoutedEventArgs e) {

            //Grafo.GetGrafo().DibujarVertices();

            //Grafo.GetGrafo().EnviarSolicitudes();
        }
    }
}
