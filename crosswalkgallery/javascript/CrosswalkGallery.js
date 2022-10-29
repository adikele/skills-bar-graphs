import React from 'react'
import { Zoom } from 'react-awesome-reveal'
import { Fade } from 'react-awesome-reveal'
import { Bounce } from 'react-awesome-reveal'
import { Roll } from 'react-awesome-reveal'

const CrosswalkGallery = () => {
    const width = '70%';
    const height = '70%';

    return (
        <div>
            <Zoom>
                <div>
                    <img
                        className='img-responsive'
                        width={width}
                        height={height}
                        src={require('../static/img/calle-jose-betancort-g2f3500339_1280.jpg')}
                        alt='img'
                    />
                </div>
            </Zoom>

            <Fade>
                <div>
                    <img
                        className='img-responsive'
                        width={width}
                        height={height}
                        src={require('../static/img/crossing-gfc54c11d8_1280.jpg')}
                        alt='img'
                    />
                </div>
            </Fade>

            <Bounce>
                <div>
                    <img
                        className='img-responsive'
                        width={width}
                        height={height}
                        src={require('../static/img/crosswalk-gb964a0024_1280.jpg')}
                        alt='img'
                    />
                </div>
            </Bounce>

            <Fade>
                <div>
                    <img
                        className='img-responsive'
                        width={width}
                        height={height}
                        src={require('../static/img/elephant-gcc3152380_1280.jpg')}
                        alt='img'
                    />
                </div>
            </Fade>

            <Roll>
                <div>
                    <img
                        className='img-responsive'
                        width={width}
                        height={height}
                        src={require('../static/img/square-g63ae3b358_1280.jpg')}
                        alt='img'
                    />
                </div>
            </Roll>

            <Fade>
                <div>
                    <img
                        className='img-responsive'
                        width={width}
                        height={height}
                        src={require('../static/img/traffic-light-g7fe360c01_1280.jpg')}
                        alt='img'
                    />
                </div>
            </Fade>

        </div>
    )
}

export default CrosswalkGallery