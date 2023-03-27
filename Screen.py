from tkinter import Canvas
import random
import math

canvas = Canvas(width=800, height=800, bg="white")

lines = []
delta = []


def draw_path_dijkstra(path_dijkstra, points):
    for z in range(len(path_dijkstra)):
        xcoor3 = points[path_dijkstra[z]][0]
        ycoor3 = points[path_dijkstra[z]][1]
        try:
            xcoor4 = points[path_dijkstra[z + 1]][0]
            ycoor4 = points[path_dijkstra[z + 1]][1]
        except:
            canvas.create_oval(xcoor3 - 3, ycoor3 - 4, xcoor3 + 19, ycoor3 - 26, width=4, outline="Blue",
                               fill="Blue")
            canvas.create_text(xcoor3 + 8, ycoor3 - 15, text=path_dijkstra[z], font=("Arial", 15),
                               fill="white")  # create text
            canvas.create_oval(xcoor3 - 5, ycoor3 - 5, xcoor3 + 5, ycoor3 + 5, width=2, outline="Black", fill="Blue")
            break

        canvas.create_line(xcoor3, ycoor3, xcoor4, ycoor4, width=5, fill="Blue")
        canvas.create_oval(xcoor3 - 3, ycoor3 - 4, xcoor3 + 19, ycoor3 - 26, width=4, outline="Blue", fill="Blue")
        canvas.create_text(xcoor3 + 8, ycoor3 - 15, text=path_dijkstra[z], font=("Arial", 15),
                           fill="white")  # create text
        canvas.create_oval(xcoor3 - 5, ycoor3 - 5, xcoor3 + 5, ycoor3 + 5, width=2, outline="Black", fill="Blue")

def draw_path_a_star(path_a_star, points):
    for z in range(len(path_a_star)):
        xcoor3 = points[path_a_star[z]][0]
        ycoor3 = points[path_a_star[z]][1]
        try:
            xcoor4 = points[path_a_star[z + 1]][0]
            ycoor4 = points[path_a_star[z + 1]][1]
        except:
            canvas.create_oval(xcoor3 - 3, ycoor3 - 4, xcoor3 + 19, ycoor3 - 26, width=4, outline="Orange",
                               fill="Orange")
            canvas.create_text(xcoor3 + 8, ycoor3 - 15, text=path_a_star[z], font=("Arial", 15),
                               fill="white")  # create text
            canvas.create_oval(xcoor3 - 5, ycoor3 - 5, xcoor3 + 5, ycoor3 + 5, width=2, outline="Black", fill="Orange")
            break

        canvas.create_line(xcoor3, ycoor3, xcoor4, ycoor4, width=5, fill="Orange")
        canvas.create_oval(xcoor3 - 3, ycoor3 - 4, xcoor3 + 19, ycoor3 - 26, width=4, outline="Orange", fill="Orange")
        canvas.create_text(xcoor3 + 8, ycoor3 - 15, text=path_a_star[z], font=("Arial", 15),
                           fill="white")  # create text
        canvas.create_oval(xcoor3 - 5, ycoor3 - 5, xcoor3 + 5, ycoor3 + 5, width=2, outline="Black", fill="Orange")


def distance(points, num1, num2):
    p = [points[num1][0], points[num1][1]]
    q = [points[num2][0], points[num2][1]]
    return math.dist(p, q)


def initUI(points, point_num, space_min, con_low, con_high, double_chance, graph, delta_fluctuation, rota):
    a_bet = [ind for ind in range(point_num)]

    def draw_points(points):
        for k in range(len(points)):
            canvas.create_oval(points[k][0] - 3, points[k][1] - 4, points[k][0] + 19, points[k][1] - 26, width=1,
                               fill="#FFFFFF")  # create white
            canvas.create_text(points[k][0] + 8, points[k][1] - 15, text=a_bet[k], font=("Arial", 15))  # create text
            canvas.create_oval(points[k][0] + 5, points[k][1] + 5, points[k][0] - 5, points[k][1] - 5, width=2,
                               fill="#FFFFFF")  # create oval

    def drawline_single(coorx1, coorx2, coory1, coory2):
        canvas.create_line(coorx1, coory1, coorx2, coory2, width=2, dash=(5, 5, 2, 1), dashoff=10, fill="Black")

        mid_x = (coorx1 + coorx2) / 2
        mid_y = (coory1 + coory2) / 2
        angle = math.atan2(coory2 - coory1, coorx2 - coorx1)
        canvas.create_polygon(mid_x + 12 * math.cos(angle + -3.5),
                              mid_y + 12 * math.sin(angle + -3.5),
                              mid_x, mid_y,
                              mid_x + 12 * math.cos(angle - -3.5),
                              mid_y + 12 * math.sin(angle - -3.5),
                              fill="black")

    def drawline_double(coorx1, coorx2, coory1, coory2, sp):
        if coory1 == coory2:
            coory2 += 1
        angle = math.atan((coorx1 - coorx2) / (coory1 - coory2)) + 0.5 * math.pi
        x1 = sp * math.sin(angle)
        y1 = sp * math.cos(angle)
        x2 = sp * math.sin(angle + math.pi)
        y2 = sp * math.cos(angle + math.pi)

        canvas.create_line(coorx1 + x1, coory1 + y1, coorx2 - x2, coory2 - y2, width=2, dash=(5, 5, 2, 1), dashoff=10)
        canvas.create_line(coorx1 - x1, coory1 - y1, coorx2 + x2, coory2 + y2, width=2, dash=(5, 5, 2, 1), dashoff=10)

        mid_x1 = (coorx1 + x1 + coorx2 - x2) / 2
        mid_y1 = (coory1 + y1 + coory2 - y2) / 2
        mid_x2 = (coorx1 - x1 + coorx2 + x2) / 2
        mid_y2 = (coory1 - y1 + coory2 + y2) / 2

        angle = math.atan2(coory2 - coory1, coorx2 - coorx1)

        canvas.create_polygon(mid_x1 + 12 * math.cos(angle + -3.5),
                              mid_y1 + 12 * math.sin(angle + -3.5),
                              mid_x1, mid_y1,
                              mid_x1 + 12 * math.cos(angle - -3.5),
                              mid_y1 + 12 * math.sin(angle - -3.5), fill="black")

        canvas.create_polygon(mid_x2 + 12 * math.cos(angle + -0.4),
                              mid_y2 + 12 * math.sin(angle + -0.4),
                              mid_x2, mid_y2,
                              mid_x2 + 12 * math.cos(angle - -0.4),
                              mid_y2 + 12 * math.sin(angle - -0.4), fill="black")

    while len(points) < point_num:
        rand_xy = [random.randint(20, 780), random.randint(20, 780)]
        xy_temp = [1000]
        for j in range(len(points)):
            xy_temp.append(math.dist(rand_xy, points[j]))

        xy_temp.sort()

        if xy_temp[0] < space_min:
            pass

        else:
            print(len(points))
            points.append([rand_xy[0], rand_xy[1]])

    while len(points) < point_num:
        rand_xy = [random.randint(20, 780), random.randint(20, 780)]
        xy_temp = []
        for j in range(len(points) + 1):
            xy_temp.append(math.dist(rand_xy, points[j]))
        xy_temp.sort()

        if xy_temp[0] < space_min:
            pass
        else:
            print(len(points))
            canvas.create_text(rand_xy[0] + 8, rand_xy[1] - 15, text=a_bet[len(points)],
                               font=("Arial", 15))  # create text
            canvas.create_oval(rand_xy[0] + 5, rand_xy[1] + 5, rand_xy[0] - 5, rand_xy[1] - 5, width=2,
                               fill="#FFFFFF")  # create oval
            points.append([rand_xy[0], rand_xy[1]])

    print('created points')
    temp_delta = []

    # p1 = 380 - rota
    # p2 = 380 + rota
    #
    points[0][0] = 520
    points[0][1] = 620
    points[1][0] = 80
    points[1][1] = 100


    for num1 in range(point_num):  # create lines
        temp_distance = []
        for num2 in range(point_num):
            if num1 == num2:
                temp_distance.append(16383 * delta_fluctuation)
            else:
                temp_distance.append(round(distance(points, num1, num2)))
        delta.append(temp_distance.copy())
        temp_delta.append(temp_distance.copy())

    print('created lines')

    for b in range(point_num):
        temp_lines = []
        for a in range(con_high):  # lowest numbers
            lowest = min(temp_delta[b])
            lowest_index = temp_delta[b].index(lowest)
            temp_lines.append(lowest_index)
            temp_delta[b].pop(lowest_index)
            temp_delta[b].insert(lowest_index, 1000)
        lines.append(temp_lines)

    print('lowest number')

    connected_single = []
    connected_double = []

    for s in range(point_num):
        for d in range(random.randint(con_low, con_high)):
            connected_temp = []
            connected_temp2 = []
            connected_temp.append(s)
            connected_temp.append(lines[s][d])
            connected_temp2.append(lines[s][d])
            connected_temp2.append(s)

            if connected_temp in connected_single or connected_temp in connected_double or connected_temp2 in connected_double or connected_temp2 in connected_single:
                pass

            elif random.randint(0, 100) <= double_chance:
                graph[connected_temp[0]][connected_temp[1]] = delta[connected_temp[0]][connected_temp[1]]
                graph[connected_temp[1]][connected_temp[0]] = delta[connected_temp[0]][connected_temp[1]]
                connected_double.append(connected_temp)

            else:
                graph[connected_temp[0]][connected_temp[1]] = delta[connected_temp[0]][connected_temp[1]]
                connected_single.append(connected_temp)

    print('connections made')

    for k in range(point_num):
        for l in range(point_num):
            graph_value_temp = graph[k][l]
            if graph_value_temp != None:
                graph[k][l] = graph_value_temp * random.randint(1,delta_fluctuation)
            else:
                pass


    for h in range(len(connected_single)):
        coorx1 = points[connected_single[h][0]][0]
        coory1 = points[connected_single[h][0]][1]
        coorx2 = points[connected_single[h][1]][0]
        coory2 = points[connected_single[h][1]][1]
        drawline_single(coorx1, coorx2, coory1, coory2)

    print('single lines drawn')

    for h in range(len(connected_double)):
        coorx1 = points[connected_double[h][0]][0]
        coory1 = points[connected_double[h][0]][1]
        coorx2 = points[connected_double[h][1]][0]
        coory2 = points[connected_double[h][1]][1]
        drawline_double(coorx1, coorx2, coory1, coory2, sp=4)

    print('double lines drawn')


    draw_points(points)
    canvas.pack(pady=10)
