import gps

# Listen to gpsd on port 2947
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

while True:
	try:
		report = session.next()
			#Narrow fields with classes
			#To see everything, uncomment the line below
			#print report
		if report['class'] = 'TPV':
			#if hasattr(report, 'time'):
				#print report.time
			if hassattr(report, 'speed'):
				print report.speed * gps.MPS_TO_KPH
	except KeyError:
		pass
	except KeyboardInterrupt:
		quit()
	except StopIteration:
		session = None
		print "GPSD Timeout"