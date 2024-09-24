def better_than_average(class_points, your_points):
    total=your_points
    for point in class_points:
        total+=point
    avg = total/(len(class_points)+1)
    return your_points > avg