from app import db, load_stops

db.create_all()
stop_list = np.array(load_stops.collect_stops())
for stop in stop_list:
	db.session.add(stop)

db.session.commit()